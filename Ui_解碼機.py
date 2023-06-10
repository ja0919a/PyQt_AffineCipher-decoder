# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '解碼機.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 450)
        self.horizontalLayout_9 = QHBoxLayout(Form)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_1 = QRadioButton(Form)
        self.radioButton_1.setObjectName(u"radioButton_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        self.radioButton_1.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_1)

        self.horizontalSpacer = QSpacerItem(95, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_func = QLabel(Form)
        self.label_func.setObjectName(u"label_func")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_func.sizePolicy().hasHeightForWidth())
        self.label_func.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_func.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_func)

        self.horizontalSpacer_4 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_m = QLabel(Form)
        self.label_m.setObjectName(u"label_m")
        sizePolicy1.setHeightForWidth(self.label_m.sizePolicy().hasHeightForWidth())
        self.label_m.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_m)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_a = QLineEdit(Form)
        self.lineEdit_a.setObjectName(u"lineEdit_a")

        self.horizontalLayout_5.addWidget(self.lineEdit_a)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_b = QLineEdit(Form)
        self.lineEdit_b.setObjectName(u"lineEdit_b")

        self.horizontalLayout_5.addWidget(self.lineEdit_b)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.mod_lineEdit = QLineEdit(Form)
        self.mod_lineEdit.setObjectName(u"mod_lineEdit")

        self.horizontalLayout_2.addWidget(self.mod_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboBox_case = QComboBox(Form)
        self.comboBox_case.setObjectName(u"comboBox_case")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_case.sizePolicy().hasHeightForWidth())
        self.comboBox_case.setSizePolicy(sizePolicy2)
        self.comboBox_case.setMinimumSize(QSize(138, 0))

        self.horizontalLayout_6.addWidget(self.comboBox_case)

        self.comboBox_foreign = QComboBox(Form)
        self.comboBox_foreign.setObjectName(u"comboBox_foreign")
        sizePolicy2.setHeightForWidth(self.comboBox_foreign.sizePolicy().hasHeightForWidth())
        self.comboBox_foreign.setSizePolicy(sizePolicy2)
        self.comboBox_foreign.setMinimumSize(QSize(141, 0))

        self.horizontalLayout_6.addWidget(self.comboBox_foreign)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.InputTextEdit = QTextEdit(Form)
        self.InputTextEdit.setObjectName(u"InputTextEdit")
        self.InputTextEdit.setMinimumSize(QSize(0, 220))

        self.horizontalLayout_8.addWidget(self.InputTextEdit)

        self.OutputTextEdit = QPlainTextEdit(Form)
        self.OutputTextEdit.setObjectName(u"OutputTextEdit")
        self.OutputTextEdit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.OutputTextEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_6.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_6)

        self.SystemTextEdit = QPlainTextEdit(Form)
        self.SystemTextEdit.setObjectName(u"SystemTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SystemTextEdit.sizePolicy().hasHeightForWidth())
        self.SystemTextEdit.setSizePolicy(sizePolicy3)
        self.SystemTextEdit.setMaximumSize(QSize(16777215, 130))
        font2 = QFont()
        font2.setPointSize(12)
        self.SystemTextEdit.setFont(font2)
        self.SystemTextEdit.setAutoFillBackground(False)
        self.SystemTextEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.SystemTextEdit)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Affine Cipher \u89e3\u78bc\u6a5f", None))
        self.radioButton_1.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u89e3\u78bc", None))
        self.label_func.setText(QCoreApplication.translate("Form", u"\u516c\u5f0f : E(x)=(ax+b) mod m              ", None))
        self.label_m.setText(QCoreApplication.translate("Form", u"m=26", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"a=", None))
        self.lineEdit_a.setText(QCoreApplication.translate("Form", u"5", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"b=", None))
        self.lineEdit_b.setText(QCoreApplication.translate("Form", u"8", None))
        self.label.setText(QCoreApplication.translate("Form", u"mod=", None))
        self.mod_lineEdit.setText(QCoreApplication.translate("Form", u"abcdefghijklmnopqrstuvwxyz", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"mod\u4ee5\u5916\u7684\u5b57\u5143", None))
        self.InputTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u9019\u88e1\u8f38\u5165", None))
        self.OutputTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u9019\u908a\u6703\u8f38\u51fa", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5831\u932f", None))
#if QT_CONFIG(tooltip)
        self.SystemTextEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.SystemTextEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.SystemTextEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SystemTextEdit.setPlainText("")
        self.SystemTextEdit.setPlaceholderText("")
    # retranslateUi

