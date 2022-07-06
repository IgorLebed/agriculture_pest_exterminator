from PySide6 import QtGui, QtCore, QtWidgets

class WinPosExplore(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Plastique"))
        QtWidgets.QWidget.__init__(self)
        self.show()

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            winPos=self.pos() 
            globalWinPos = self.mapToGlobal(winPos)  
            msg1="winPos=self.pos(): <{0}, {1}>\n".format(winPos.x(), winPos.y())
            msg2="self.mapToGlobal(winPos): <{0}, {1}>\n\n".format(globalWinPos.x(), globalWinPos.y())
            print(msg1 + msg2)

def main():
    import sys
    qtApp=QtWidgets.QApplication(sys.argv)
    myWinPos=WinPosExplore()
    sys.exit(qtApp.exec_())

if __name__=="__main__":
    main()