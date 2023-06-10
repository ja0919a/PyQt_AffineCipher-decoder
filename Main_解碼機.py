from PySide6.QtWidgets import QApplication,QMainWindow,QWidget
from Ui_解碼機 import Ui_Form
from PySide6.QtGui import QIntValidator
from AffineCipher import encode,decode

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_case.addItems(['維持大小寫格式','忽略大小寫格式','大小寫分開辨識(A ≠ a)'])
        self.comboBox_case.setCurrentIndex(0)
        self.comboBox_foreign.addItems(['維持mod以外的字元','忽略mod以外的字元'])
        self.comboBox_foreign.setCurrentIndex(0)
        self.lineEdit_a.setValidator(QIntValidator())
        self.lineEdit_b.setValidator(QIntValidator())
        self.bind()
        
    def bind(self):
        self.comboBox_case.currentIndexChanged.connect(self.change)
        self.comboBox_foreign.currentIndexChanged.connect(self.change)
        self.radioButton_1.clicked.connect(self.change)
        self.radioButton_2.clicked.connect(self.change)
        self.mod_lineEdit.textChanged.connect(self.change)
        self.lineEdit_a.textChanged.connect(self.change)
        self.lineEdit_b.textChanged.connect(self.change)
        self.InputTextEdit.textChanged.connect(self.change)
    def isCoprime(self,a,b):
        if b==0:
            return a==1
        return self.isCoprime(b,a%b)
    def detect(self):
        if self.lineEdit_a.text()=='' or self.lineEdit_b.text()=='' or self.mod_lineEdit.text()=='':
            self.SystemTextEdit.setPlainText('請輸入a,b,mod!!!')
            return False
        if self.comboBox_case.currentIndex()==0 or self.comboBox_case.currentIndex()==1:
            mod=self.mod_lineEdit.text().lower()
            for i in range(len(mod)):
                if mod.count(mod[i])>1:
                    self.SystemTextEdit.setPlainText('mod中不可有重複字元!!!')
                    return False
        if self.comboBox_case.currentIndex()==2:
            mod=self.mod_lineEdit.text()
            for i in range(len(mod)):
                if mod.count(mod[i])>1:
                    self.SystemTextEdit.setPlainText('mod中不可有重複字元!!!')
                    return False
        if self.lineEdit_a.text()=='1' or len(self.mod_lineEdit.text())==1:
            self.SystemTextEdit.setPlainText('a與mod長度需互質!!!')
            return False
        if not self.isCoprime(int(self.lineEdit_a.text()),len(self.mod_lineEdit.text())):
            self.SystemTextEdit.setPlainText('a與mod長度需互質!!!')
            return False
        return True
        
    def change(self):
        self.label_m.setText('m='+str(len(self.mod_lineEdit.text())))
        self.SystemTextEdit.setPlainText('')
        if self.radioButton_1.isChecked():
            self.label_func.setText('公式 : E(x)=(ax+b) mod m              ')
        else:
            self.label_func.setText('公式 : D(x)=a^-1(x-b) mod m')
        if self.detect():
            mod=self.mod_lineEdit.text()
            a=int(self.lineEdit_a.text())
            b=int(self.lineEdit_b.text())
            if self.radioButton_1.isChecked():
                self.OutputTextEdit.setPlainText(encode(self.InputTextEdit.toPlainText(),mod,a,b,self.comboBox_case.currentIndex(),self.comboBox_foreign.currentIndex()))
            else:
                self.OutputTextEdit.setPlainText(decode(self.InputTextEdit.toPlainText(),mod,a,b,self.comboBox_case.currentIndex(),self.comboBox_foreign.currentIndex()))
        

if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()