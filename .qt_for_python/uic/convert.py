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
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_ConvertTextTitle(object):
    def setupUi(self, ConvertTextTitle):
        if not ConvertTextTitle.objectName():
            ConvertTextTitle.setObjectName(u"ConvertTextTitle")
        ConvertTextTitle.resize(922, 629)
        self.raw_text_label = QLabel(ConvertTextTitle)
        self.raw_text_label.setObjectName(u"raw_text_label")
        self.raw_text_label.setGeometry(QRect(10, 10, 58, 16))
        self.raw_text_editor = QPlainTextEdit(ConvertTextTitle)
        self.raw_text_editor.setObjectName(u"raw_text_editor")
        self.raw_text_editor.setGeometry(QRect(0, 30, 921, 191))
        self.result_label = QLabel(ConvertTextTitle)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(10, 230, 71, 16))
        self.sure_button = QPushButton(ConvertTextTitle)
        self.sure_button.setObjectName(u"sure_button")
        self.sure_button.setGeometry(QRect(849, 220, 61, 32))
        self.result_text_browser = QTextBrowser(ConvertTextTitle)
        self.result_text_browser.setObjectName(u"result_text_browser")
        self.result_text_browser.setGeometry(QRect(0, 250, 921, 341))
        self.pushButton_2 = QPushButton(ConvertTextTitle)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(820, 590, 100, 32))

        self.retranslateUi(ConvertTextTitle)

        QMetaObject.connectSlotsByName(ConvertTextTitle)
    # setupUi

    def retranslateUi(self, ConvertTextTitle):
        ConvertTextTitle.setWindowTitle(QCoreApplication.translate("ConvertTextTitle", u"Form", None))
        self.raw_text_label.setText(QCoreApplication.translate("ConvertTextTitle", u"\u539f\u6587:", None))
        self.result_label.setText(QCoreApplication.translate("ConvertTextTitle", u"\u7ed3\u679c\uff1a", None))
        self.sure_button.setText(QCoreApplication.translate("ConvertTextTitle", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("ConvertTextTitle", u"\u5bfc\u51fatxt", None))
    # retranslateUi

