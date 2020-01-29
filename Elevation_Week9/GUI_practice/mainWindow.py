import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel
from ui_mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Rebecca's first window!")
        self.ui.pushBtn.clicked.connect(self.on_pushButton)

    def on_pushButton(self):
        # name = self.ui.textEdit1.text()
        # self.ui.label3.setText("Welcome " + name)

        names = ["Ariel", "David", "Ana", "Oren"]
        random.choice(names)
        self.ui.pushBtn.setText(random.choice(names))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())

main()