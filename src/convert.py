# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_ConvertTextTitle(object):
    def setupUi(self, ConvertTextTitle):
        if not ConvertTextTitle.objectName():
            ConvertTextTitle.setObjectName(u"ConvertTextTitle")
        ConvertTextTitle.resize(937, 688)
        self.raw_text_label = QLabel(ConvertTextTitle)
        self.raw_text_label.setObjectName(u"raw_text_label")
        self.raw_text_label.setGeometry(QRect(10, 10, 58, 16))
        self.raw_text_editor = QPlainTextEdit(ConvertTextTitle)
        self.raw_text_editor.setObjectName(u"raw_text_editor")
        self.raw_text_editor.setGeometry(QRect(10, 30, 921, 191))
        self.result_label = QLabel(ConvertTextTitle)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(10, 240, 71, 16))
        self.sure_button = QPushButton(ConvertTextTitle)
        self.sure_button.setObjectName(u"sure_button")
        self.sure_button.setGeometry(QRect(870, 230, 61, 32))
        self.result_text_browser = QTextBrowser(ConvertTextTitle)
        self.result_text_browser.setObjectName(u"result_text_browser")
        self.result_text_browser.setGeometry(QRect(10, 270, 921, 341))
        self.save_to_txt_button = QPushButton(ConvertTextTitle)
        self.save_to_txt_button.setObjectName(u"save_to_txt_button")
        self.save_to_txt_button.setGeometry(QRect(830, 620, 100, 32))
        self.line = QFrame(ConvertTextTitle)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 650, 921, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(ConvertTextTitle)

        QMetaObject.connectSlotsByName(ConvertTextTitle)
    # setupUi

    def retranslateUi(self, ConvertTextTitle):
        ConvertTextTitle.setWindowTitle(QCoreApplication.translate("ConvertTextTitle", u"截断小程序", None))
        self.raw_text_label.setText(QCoreApplication.translate("ConvertTextTitle", u"原文:", None))
        self.result_label.setText(QCoreApplication.translate("ConvertTextTitle", u"结果", None))
        self.sure_button.setText(QCoreApplication.translate("ConvertTextTitle", u"确定", None))
        self.save_to_txt_button.setText(QCoreApplication.translate("ConvertTextTitle", u"导出txt", None))
    # retranslateUi

