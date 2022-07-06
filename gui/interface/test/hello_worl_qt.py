import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        print("AAAAAAAAAAAA")

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            winPos=self.pos() 
            globalWinPos = self.mapToGlobal(winPos)  
            msg1="winPos=self.pos(): <{0}, {1}>\n".format(winPos.x(), winPos.y())
            msg2="self.mapToGlobal(winPos): <{0}, {1}>\n\n".format(globalWinPos.x(), globalWinPos.y())
            print(msg1 + msg2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())