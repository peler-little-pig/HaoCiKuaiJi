import sys

import requests
from PyQt5.QtWidgets import QApplication, QMessageBox
from Controller.MainController import MainController
import cgitb, sys, traceback

cgitb.enable(format='text')


def my_exception_handler(exc_type, exc_value, exc_tb):
    if exc_type == requests.exceptions.ConnectionError:
        text = "请检查您的网络连接"
    else:
        text = f"意外错误，错误类型{exc_type}\n错误值{exc_value}"
    msg_box = QMessageBox.critical(None, "软件发生了一个错误", text)
    msg_box.exec_()


if __name__ == '__main__':
    sys.excepthook = my_exception_handler
    app = QApplication(sys.argv)
    main_window = MainController()
    sys.exit(app.exec_())
