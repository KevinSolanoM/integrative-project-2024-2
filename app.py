import PyQt5.QtWidgets as pyqt
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap
from connect2bt import conectar


from calculator_ang import receptionDate

class Principal(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        conectar()
    
    def initGUI(self):
        uic.loadUi('canon_interfaz.ui',self)

        self.manual_menu.clicked.connect(lambda: self.isclicManual())  
        self.automatic_menu.clicked.connect(lambda: self.isclicAuto()) 
        self.ajustar_auto.clicked.connect(lambda: self.ajustarAuto())

        #valores del manual cambiados
        self.angulo_base.valueChanged.connect(lambda: self.ajustarManual())
        self.angulo_canon.valueChanged.connect(lambda: self.ajustarManual())

        #disparar:

        self.disparar_auto.clicked.connect(lambda: self.disparar())
        self.disparar_manual.clicked.connect(lambda: self.disparar())

        #recargar:
        self.recarga.clicked.connect(lambda: self.recargar())

        pixmap = QPixmap("images\logodragon.png")
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True) 

        self.image2.setPixmap(pixmap)
        self.image2.setScaledContents(True)
        
        self.show()
    
    def disparar(self):
        receptionDate(0,0,'disp')

    def recargar(self):
        receptionDate(0,0,'rec')

    def ajustarAuto(self):
        base_ang = self.barra_base_auto.value()
        distancia = self.distancia_auto.value()
        receptionDate(base_ang,distancia,'auto')
        self.recargar()

    def ajustarManual(self):
        base_ang = self.angulo_base.value()
        canon_ang = self.angulo_canon.value()
        receptionDate(base_ang,canon_ang,'manual')


    def isclicManual(self):
        self.manual_menu.setStyleSheet("background-color: rgb(03, 08, 17);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")
        self.automatic_menu.setStyleSheet("background-color: rgb(23, 28, 47);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")
        self.ajustarManual()

    def isclicAuto(self):
        self.manual_menu.setStyleSheet("background-color: rgb(23, 28, 47);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")
        self.automatic_menu.setStyleSheet("background-color: rgb(03, 08, 27);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")        
        




def main():
    app = pyqt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()