#! /usr/bin/python


from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt6.QtGui import QAction
import sys


class MDIWindow(QMainWindow):
    counter = 0

    def __init__(self):
        super().__init__()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")
        file.triggered(QAction).connect(self.WindowTrig)
        self.setWindowTitle("MDI Application")

    def WindowTrig(self, p):
        if p.text() == "New":
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit)
            sub.setWindowTitle("Sub" + str(MDIWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if p.texty() == "Cascade":
            self.mdi.cascadeSubWindows()
        if p.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mdiwindow = MDIWindow()
    mdiwindow.show()
    app.exec()
