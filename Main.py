import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt
from Evaluater import evaluate_expression

Input = ""
Answer = "0"


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.display = None
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 488)
        self.setFixedSize(300, 488)

        self.setWindowIcon(QIcon('calculator-48.png'))
        self.load_stylesheet('Style.css')
        self.create_ui()

    def load_stylesheet(self, file_path):
        with open(file_path, 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_0:
            self.NumberPressed("0")
        elif key == Qt.Key.Key_1:
            self.NumberPressed("1")
        elif key == Qt.Key.Key_2:
            self.NumberPressed("2")
        elif key == Qt.Key.Key_3:
            self.NumberPressed("3")
        elif key == Qt.Key.Key_4:
            self.NumberPressed("4")
        elif key == Qt.Key.Key_5:
            self.NumberPressed("5")
        elif key == Qt.Key.Key_6:
            self.NumberPressed("6")
        elif key == Qt.Key.Key_7:
            self.NumberPressed("7")
        elif key == Qt.Key.Key_8:
            self.NumberPressed("8")
        elif key == Qt.Key.Key_9:
            self.NumberPressed("9")
        elif key == Qt.Key.Key_Period:
            self.NumberPressed(".")
        elif key == Qt.Key.Key_Plus:
            self.NumberPressed("+")
        elif key == Qt.Key.Key_Minus:
            self.NumberPressed("-")
        elif key == Qt.Key.Key_Asterisk:
            self.NumberPressed("*")
        elif key == Qt.Key.Key_Slash:
            self.NumberPressed("/")
        elif key == Qt.Key.Key_ParenLeft:
            self.NumberPressed("(")
        elif key == Qt.Key.Key_ParenRight:
            self.NumberPressed(")")
        elif key == Qt.Key.Key_Percent:
            self.NumberPressed("%")
        elif key == Qt.Key.Key_Backspace:
            self.BackspacePressed()
        elif key == Qt.Key.Key_A:
            self.AnsPressed()
        elif key == Qt.Key.Key_C:
            self.ClearPressed()
        elif key == Qt.Key.Key_Enter:
            self.EqualsPressed()

    def create_ui(self):
        # Layouts
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)

        main_layout.addWidget(self.display)

        # Buttons
        buttons = [
            ('(', 0, 0), (')', 0, 1), ('C', 0, 2), ('⌫', 0, 3),
            ('√', 1, 0), ('x²', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('.', 5, 0), ('0', 5, 1), ('Ans', 5, 2), ('=', 5, 3),
        ]

        for button_data in buttons:
            if len(button_data) == 3:
                btn_text, row, col = button_data
                rowspan, colspan = 1, 1
            else:
                btn_text, row, col, rowspan, colspan = button_data

            button = QPushButton(btn_text)
            button.clicked.connect(self.on_button_click)
            button.setCursor(Qt.CursorShape.PointingHandCursor)

            # Set object names for styling
            if btn_text in {'7', '8', '9', '4', '5', '6', '1', '2', '3', '0'}:
                button.setObjectName('num')
            elif btn_text == '=':
                button.setObjectName('equals')
            elif btn_text == 'C':
                button.setObjectName('clear')
            elif btn_text == '⌫':
                button.setObjectName('backspace')
            else:
                button.setObjectName('op')

            grid_layout.addWidget(button, row, col, rowspan, colspan)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def on_button_click(self):
        global Input
        global Answer
        button = self.sender()
        text = button.text()

        if text == "C":
            self.ClearPressed()
        elif text == "⌫":
            self.BackspacePressed()
        elif text == "√":
            self.SqrtPressed()
        elif text == "x²":
            self.SqrPressed()
        elif text == "Ans":
            self.AnsPressed()
        elif text == "=":
            self.EqualsPressed()
        else:
            self.NumberPressed(text)

    def ClearPressed(self):
        global Answer
        global Input
        self.display.clear()
        Answer = "0"
        Input = ""

    def BackspacePressed(self):
        global Input
        Input = Input[:-1]
        self.display.setText(Input)

    def SqrtPressed(self):
        global Input
        Input = Input + "sqrt("
        self.display.setText(Input)

    def SqrPressed(self):
        global Input
        Input = Input + "sqr("
        self.display.setText(Input)

    def AnsPressed(self):
        global Input
        global Answer
        Input = Input + Answer
        self.display.setText(Input)

    def EqualsPressed(self):
        global Input
        global Answer
        if Input == "0" or Input == "Error" or Input is None:
            self.display.setText(Answer)
        try:
            result = evaluate_expression(Input)
            self.display.setText(result)
            Answer = result
            Input = ""
        except Exception as e:
            print("Error + " + str(e))
            self.display.setText("Error")
            Input = ""

    def NumberPressed(self, number):
        global Input
        Input = Input + number
        self.display.setText(Input)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
