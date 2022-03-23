# 导入程序运行必须模块
import os
import re
import sys
import random
import uuid
from typing import List
from pathlib import Path
from io import StringIO

# PySide6中使用的基本控件都在PySide6.QtWidgets模块中
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PySide6.QtGui import QTextDocumentWriter, QTextDocument
from PySide6.QtCore import Slot, QDir, QFileInfo, QCoreApplication

# 导入designer工具生成的convert模块
from convert import Ui_ConvertTextTitle
from process import newline_flag, replace_flag

# 自然语言分析
import thulac

# MIME_TYPES = ["text/html", "text/markdown", "text/plain"]
MIME_TYPES = [
    "text/plain",
]
re_book_title = re.compile(r"(《[^》]+》)")
re_quotation_mark = re.compile(r"(“[^”]+”)")


class MyMainForm(QMainWindow, Ui_ConvertTextTitle):
    def __init__(self):
        super(MyMainForm, self).__init__()
        self.setupUi(self)
        self._raw_text = ""  # 原始文本
        self._result_text = ""  # 结果文本
        self._file_name = ""
        self.book_title_map = {}
        self.user_dict_stringio = StringIO()
        self.thulac_app = None
        self.line_max_length = 20

        self.sure_button.clicked.connect(self.process_raw_text)
        self.save_to_txt_button.clicked.connect(self.file_save_as)

    def process_raw_text(self):
        self._raw_text = self.raw_text_editor.toPlainText()
        self.convert_raw_text()
        self.show_result_text()

    def convert_raw_text(self):
        self._result_text = self.cut_text(self._raw_text)

    def show_result_text(self):
        self.result_text_browser.setPlainText(self._result_text)

    def cut_text(self, sentence):
        """
        将一段文本切分成多个句子
        :param sentence: ['虽然BillRoper正忙于全新游戏
        :return: ['虽然BillRoper正..接近。' , '与父母，之首。' , '很多..常见。' , '”一位上..推进。' , ''”一直坚..市场。'' , '如今，...的70%。']

        # 近日，乘联会发布的2022年1月-2月份新能源汽车销售数据显示，前两个月国内狭义乘用车累计销量为332.4万辆，其中新能源乘用车零售销量达到61.9万辆，市场供应回暖，厂家也都在积极迎接农历新年后的“开门红”。
        """

        lines = sentence.strip().split()  # 先按照换行符分割为多行

        # 查找书名号的内容并替换
        replaced_lines = []
        for line in lines:

            if not line:
                continue

            replaced_lines.append(self.replace_book_title(line))  # 查找书名号并替换

        self.user_dict_stringio = self.book_title_to_txt()
        self.thulac_app = self.setup_user_dict()

        new_lines = []

        for line in replaced_lines:

            txt = line

            txt: str = replace_flag(txt)  # 替换为空格
            txt_arr: list = newline_flag(txt)  # 保留并换行

            for sub_txt in txt_arr:
                if sub_txt:
                    txt_arr2: list = self.split_flag(sub_txt)  # 过长的行分割

                    # 添加结果文本
                    if txt_arr2:
                        new_lines.extend(txt_arr2)

        new_centence = "\n\n".join(new_lines)
        new_centence = self.unreplace_book_title(new_centence)

        return new_centence

    def replace_book_title(self, text: str):
        # 保留双引号和书名号之间的文本

        centence = text

        # 书名号之间的内容保留
        if "《" in centence and "》" in centence:
            result = re_book_title.findall(centence)
            for book_title in result:
                rand_key = self.get_rand_key()
                self.book_title_map[rand_key] = book_title
                centence = centence.replace(book_title, rand_key)

        # 双引号之间的内容保留
        if "“" in centence and "”" in centence:
            result = re_quotation_mark.findall(centence)
            for keyword in result:
                # 当引号里面的内容大于每行长度时, 不进行保留
                if len(keyword) > self.line_max_length:
                    continue

                rand_key = self.get_rand_key()
                self.book_title_map[rand_key] = keyword
                centence = centence.replace(keyword, rand_key)

        return centence

    def unreplace_book_title(self, text: str) -> str:

        sentence = text

        for key, book_title in self.book_title_map.items():
            sentence = sentence.replace(key, book_title)

        return sentence

    def book_title_to_txt(self):
        user_dict_stringio: StringIO = StringIO()
    
        for keyword in self.book_title_map.keys():
            user_dict_stringio.write(keyword + "\n")

        return user_dict_stringio

    def setup_user_dict(self):
        return thulac.thulac(user_dict=self.user_dict_stringio, seg_only=True)  # 默认模式

    def split_flag(self, line: str):
        # 过长的行分割

        # 参考zhon 文档: https://zhon.readthedocs.io/en/latest/#using-zhon
        txt = line

        if len(txt) > self.line_max_length:
            txts = self.split_line(txt)
        else:
            txts = [
                txt,
            ]

        return ["{:>2d}:    {}".format(len(t), t.strip()) for t in txts]

    def split_line(self, line: str) -> List[str]:

        # 参考: http://thulac.thunlp.org/ 的 1.4 节
        result_arr = self.thulac_app.cut(line)  # 进行一句话分词
        word_arr = [group[0] for group in result_arr]

        centence = ""
        result_arr = []

        for word in word_arr:
            centence += word

            if len(centence) >= 10:
                result_arr.append(centence)
                centence = ""

        if len(centence) < 10:
            last = result_arr[-1]
            last += centence
            result_arr[-1] = last
        else:
            result_arr.append(centence)

        return result_arr

    def get_rand_key(self) -> str:

        key = str(uuid.uuid4()).split("-")[-1]

        if key and key in self.book_title_map and key in self._raw_text:
            return self.get_rand_key()
        else:
            return key

    def set_current_file_name(self, fileName):
        self._file_name = fileName
        # self._text_edit.document().setModified(False)

        shown_name = QFileInfo(fileName).fileName() if fileName else "未命名.txt"
        app_name = QCoreApplication.applicationName()
        self.setWindowTitle(f"{shown_name}[*] - {app_name}")
        self.setWindowModified(False)

    @Slot()
    def file_save(self):
        if not self._file_name or self._file_name.startswith(":/"):
            # return fileSaveAs()
            return self.file_save_as()

        writer = QTextDocumentWriter(self._file_name)
        # document = self._text_edit.document()
        document = QTextDocument(self._result_text)
        success = writer.write(document)
        native_fn = QDir.toNativeSeparators(self._file_name)
        if success:
            document.setModified(False)
            self.statusBar().showMessage(f'文件已保存至: "{native_fn}"')
        else:
            self.statusBar().showMessage(f'不能保存至文件: "{native_fn}"')
        return success

    @Slot()
    def file_save_as(self):
        file_dialog = QFileDialog(self, "保存为...")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)

        mime_types = MIME_TYPES
        # mime_types.insert(1, "application/vnd.oasis.opendocument.text")
        file_dialog.setMimeTypeFilters(mime_types)
        file_dialog.setDefaultSuffix("odt")
        if file_dialog.exec() != QDialog.Accepted:
            return False
        fn = file_dialog.selectedFiles()[0]
        self.set_current_file_name(fn)
        return self.file_save()


if __name__ == "__main__":
    # 固定的，PySide6程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("文本分句小程序")

    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec())
