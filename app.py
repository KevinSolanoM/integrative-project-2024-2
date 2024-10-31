import PyQt5.QtWidgets as pyqt
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap

class Principal(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
    
    def initGUI(self):
        uic.loadUi('canon_interfaz.ui',self)
        self.manual_menu.clicked.connect(lambda: self.isclic())  
        self.automatic_menu.clicked.connect(lambda: self.isclic1()) 
        self.ajustar_auto.clicked.connect(lambda: self.ajustar())

        pixmap = QPixmap("images\logodragon.png")
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True) 

        self.image2.setPixmap(pixmap)
        self.image2.setScaledContents(True)
        
        self.show()
    
    def ajustar(self):
        print('ajustado')

    def isclic(self):
        self.manual_menu.setStyleSheet("background-color: rgb(03, 08, 17);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")
        self.automatic_menu.setStyleSheet("background-color: rgb(23, 28, 47);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")


    def isclic1(self):
        self.manual_menu.setStyleSheet("background-color: rgb(23, 28, 47);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")
        self.automatic_menu.setStyleSheet("background-color: rgb(03, 08, 27);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")        
        




def main():
    app = pyqt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()