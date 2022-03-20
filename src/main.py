
#导入程序运行必须模块
import sys
#PySide6中使用的基本控件都在PySide6.QtWidgets模块中
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PySide6.QtGui import QTextDocumentWriter, QTextDocument
from PySide6.QtCore import Slot, QDir, QFileInfo, QCoreApplication

#导入designer工具生成的convert模块
from convert import Ui_ConvertTextTitle

# MIME_TYPES = ["text/html", "text/markdown", "text/plain"]
MIME_TYPES = ["text/plain", ]

class MyMainForm(QMainWindow, Ui_ConvertTextTitle):
    def __init__(self):
        super(MyMainForm, self).__init__()
        self.setupUi(self)
        self._raw_text = ''  # 原始文本
        self._result_text = ''  # 结果文本
        self._file_name = ''

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
        """

        lines = sentence.strip().split()

        delimiters = ['，', '.',  '。', '！', '？', '?', ',', ';']

        new_lines = []

        for line in lines:
            txt = line
            for delimiter in delimiters:
                txt = txt.replace(f'{delimiter}', f'{delimiter}\n\n')
            new_lines.append(txt)
        
        new_centence = '\n'.join(new_lines) 

        return new_centence

    
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
        document = QTextDocument(self._raw_text)
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
        file_dialog = QFileDialog(self, "Save as...")
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
    #固定的，PySide6程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("文本分句小程序")

    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec())