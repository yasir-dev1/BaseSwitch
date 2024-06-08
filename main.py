import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog,QApplication


class App(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("GUI.ui",self)
        self.bases = {
            "Dec":10,
            "Hex":16,
            "Oct":8,
            "Bin":2,
        }
        self.number = None
        self.result = ""
        self.fromb = self.bases[self.from_base.currentText()]
        self.tob = self.bases[self.to_base.currentText()]

        self.from_base.currentIndexChanged.connect(self.onComboBoxChanged)
        self.to_base.currentIndexChanged.connect(self.onComboBoxChanged)
        self.Num.textChanged.connect(self.on_text_changed)
        self.convert_btn.clicked.connect(self.convert_operation)

    def onComboBoxChanged(self):
        self.fromb = self.bases[self.from_base.currentText()]
        self.tob = self.bases[self.to_base.currentText()]


    def on_text_changed(self,text):
        self.number = text

    def convert_operation(self):
        if self.number is not None:
            try:
                decimal_number = int(self.number,self.fromb)
            except ValueError:
                self.result = "Invaild input Please provide the input number in the correct form at for the specified base"
            
            while decimal_number > 0:
                remainder = decimal_number % self.tob
                self.result = str(remainder) + self.result
                decimal_number //= self.tob
        else:
            self.result = "Please Enter The Data"
        self.result_te.setPlainText(self.result)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.setWindowTitle("BaseSwitch")
    window.show()
    sys.exit(app.exec())