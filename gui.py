from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QLabel,
    QComboBox,
    QPushButton,
    QLineEdit
)
from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QRegularExpressionValidator
from units import weight, length
import sys

__version__ = "1.0.0"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Configure main window
        self.setWindowTitle(f"Uniter v{__version__}")
        self.setGeometry(50, 50, 350, 500)
        self.setMaximumSize(350, 500)
        self.setFixedSize(350, 500)

        frm = Convert(self)
        frm.show()


class Convert(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setGeometry(0, 0, 350, 500)
        self.setStyleSheet(
            """
                QFrame {
                background-color: #CFD8DC;
                }
                QLabel {
                background-color: #263238;
                color: #eceff1;
                font-weight: bold;
                border-radius: 5px;
                font-size: 15px;
                }
                QPushButton {
                background-color: #37474F;
                color: #ECEFF1;
                border-radius: 5px;
                font-weight: bold;
                font-size: 25px;
                }
                QPushButton:hover {
                background-color: #2E7D32;
                color: #DCEDC8;
                }
                QComboBox {
                border: 2px solid #263238;
                border-radius: 5px;
                }
                QComboBox QAbstractItemView {
                border-radius: 5px;
                background-color: #DCEDC8;
                }
                QLineEdit {
                border-radius: 5px;
                font-size: 25px;
                }
            """
        )
        self.lbl_unit_type = QLabel(text="Unit type: ", parent=self)
        self.lbl_unit_type.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter
        )
        self.lbl_unit_type.setGeometry(10, 10, 165, 40)

        self.list_unit_type = QComboBox(self)
        self.list_unit_type.setGeometry(177, 10, 165, 40)
        self.list_unit_type.addItems(["weight", "length"])
        self.list_unit_type.currentTextChanged.connect(self.current_item)

        self.lbl_convert_from = QLabel(text="From: ", parent=self)
        self.lbl_convert_from.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter
        )
        self.lbl_convert_from.setGeometry(10, 70, 63, 40)

        self.list_convert_from = QComboBox(self)
        self.list_convert_from.setGeometry(75, 70, 100, 40)
        self.list_convert_from.addItems(weight.get_aliases())

        self.lbl_convert_to = QLabel(text="To: ", parent=self)
        self.lbl_convert_to.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter
        )
        self.lbl_convert_to.setGeometry(177, 70, 63, 40)

        self.list_convert_to = QComboBox(self)
        self.list_convert_to.setGeometry(242, 70, 100, 40)
        self.list_convert_to.addItems(weight.get_aliases())

        self.unit_amount = QLineEdit(self)
        self.unit_amount.setFocus()
        self.unit_amount.setValidator(
            QRegularExpressionValidator(r"[\d*]+[\.{1}][\d*]+")
        )
        self.unit_amount.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.unit_amount.setGeometry(10, 160, 330, 40)

        self.result = QLabel(self)
        self.result.setGeometry(10, 220, 330, 40)
        self.result.setStyleSheet(
            """
                QLabel {
                background-color: #E0E0E0;
                color: #212121;
                }
            """
        )
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.convert_btn = QPushButton(text="Convert", parent=self)
        self.convert_btn.clicked.connect(self.convert)
        self.convert_btn.setGeometry(10, 300, 330, 40)

    def convert(self):
        def str2number(numb: str) -> float | int:
            result = 0

            if numb == "":
                result = 0
            elif "." in numb:
                result = float(numb)
            else:
                result = int(numb)

            return result

        inp_value = str2number(self.unit_amount.text())
        unit_from = self.list_convert_from.currentText()
        unit_to = self.list_convert_to.currentText()
        res = ""

        match unit_from:
            case "g":
                g = weight.Gram(inp_value)
                res = f"{g.convert_to(unit_to)}{unit_to}"
            case "kg":
                kg = weight.Kilogram(inp_value)
                res = f"{kg.convert_to(unit_to)}{unit_to}"
            case "mm":
                mm = length.Millimeter(inp_value)
                res = f"{mm.convert_to(unit_to)}{unit_to}"
            case "cm":
                cm = length.Centimeter(inp_value)
                res = f"{cm.convert_to(unit_to)}{unit_to}"
            case "m":
                m = length.Meter(inp_value)
                res = f"{m.convert_to(unit_to)}{unit_to}"
            case "km":
                km = length.Kilometer(inp_value)
                res = f"{km.convert_to(unit_to)}{unit_to}"

        self.result.setText(res)

    def current_item(self, i):
        match i:
            case "weight":
                self.list_convert_from.clear()
                self.list_convert_to.clear()
                self.list_convert_from.addItems(weight.get_aliases())
                self.list_convert_to.addItems(weight.get_aliases())

            case "length":
                self.list_convert_from.clear()
                self.list_convert_to.clear()
                self.list_convert_from.addItems(length.get_aliases())
                self.list_convert_to.addItems(length.get_aliases())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()
