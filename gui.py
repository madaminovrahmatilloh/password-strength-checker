import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QVBoxLayout
)

from core import analyze_password


class PasswordCheckerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Strength Checker")
        self.setFixedSize(350, 220)

        self.label = QLabel("Enter password:")
        self.input = QLineEdit()
        self.input.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("Check Strength")
        self.button.clicked.connect(self.check_password)

        self.result = QLabel("")
        self.result.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def check_password(self):
        password = self.input.text()

        if not password:
            self.result.setText("Please enter a password.")
            return

        data = analyze_password(password)

        text = (
            f"Strength: {data['strength']}\n"
            f"Score: {data['score']}\n"
            f"Crack Time: {data['crack_time']}"
        )

        if data["common"]:
            text += "\n Common password!"

        self.result.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordCheckerGUI()
    window.show()
    sys.exit(app.exec_())
