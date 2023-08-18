from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTextBrowser, QTextEdit, QDialogButtonBox


class ContentDialog(QDialog):
    def __init__(self, content):
        super().__init__()
        self.setWindowTitle("详细信息")
        self.setGeometry(100, 100, 500, 600)

        self.init_ui(content)

    def init_ui(self, content):
        layout = QVBoxLayout()

        label = QTextEdit()
        label.setText(content)
        layout.addWidget(label)

        button = QDialogButtonBox()
        button.accepted.connect(self.accept)
        button.rejected.connect(self.reject)
        layout.addWidget(button)

        self.setLayout(layout)