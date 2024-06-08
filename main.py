import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QDialog

class App(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("GUI.ui", self)
        self.bases = {
            "Dec": 10,
            "Hex": 16,
            "Bin": 2,
            "Oct": 8
        }
        self.number = None
        self.from_base = self.bases[self.fromb.currentText()]
        self.to_base = self.bases[self.to.currentText()]
        self.result = None

        self.fromb.currentIndexChanged.connect(self.onComboBoxChanged)
        self.to.currentIndexChanged.connect(self.onComboBoxChanged)
        self.convert.clicked.connect(self.convert_operation)
        self.num.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        self.number = text

    def onComboBoxChanged(self):
        self.from_base = self.bases[self.fromb.currentText()]
        self.to_base = self.bases[self.to.currentText()]
    
    def convert_operation(self):
        if self.number is not None and self.from_base is not None and self.to_base is not None:
            if not isinstance(self.number, str) or not isinstance(self.from_base, int) or not isinstance(
                    self.to_base, int):
                return "The input number should be a string, and bases should be integers."
            if self.from_base < 2 or self.from_base > 16 or self.to_base < 2 or self.to_base > 16:
                return "Bases should be between 2 and 16 inclusively."

            try:
                decimal_number = int(self.number, self.from_base)
            except ValueError:
                return "Invalid input. Please provide the input number in the correct format for the specified base."

            self.result = ""
            while decimal_number > 0:
                remainder = decimal_number % self.to_base
                self.result = str(remainder) + self.result
                decimal_number //= self.to_base
        else:
            self.result = "Please Enter The Num and"
        self.rs.setText(self.result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.setWindowTitle("BaseSwitch")
    window.show()
    sys.exit(app.exec())
