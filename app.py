import PyQt5.QtWidgets as pyqt
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap
from connect2bt import conectar
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import time

from calculator_ang import receptionDate

class Principal(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        
        self.mode = None
        self.cone = conectar()
        self.setCon()
    
    def initGUI(self):
        uic.loadUi('canon_interfaz.ui',self)
        #self.info.setText(self.cone)
        self.setWindowTitle('Control De Cañon')
        self.setWindowIcon(QIcon('images/logodragon.png'))    

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

        #atajos de teclado
        self.shortcut_up = pyqt.QShortcut(QKeySequence(Qt.Key_Up), self)
        self.shortcut_up.activated.connect(self.clicteclaUp)

        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Down), self)
        self.shortcut_down.activated.connect(self.clicteclaDown)
        
        self.shortcut_up = pyqt.QShortcut(QKeySequence(Qt.Key_Left), self)
        self.shortcut_up.activated.connect(self.clicteclaLeft)
        
        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Right), self)
        self.shortcut_down.activated.connect(self.clicteclaRight)

        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Space), self)
        self.shortcut_down.activated.connect(self.recarga.click)
        
        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut_down.activated.connect(lambda: self.disparar())
        
        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Tab), self)
        self.shortcut_down.activated.connect(lambda: self.chageMode())

        self.show()

    
    def chageMode(self):
        if self.mode == None:
            self.manual_menu.click()
        elif self.mode == 'manual':
            self.automatic_menu.click()
        else:
            self.manual_menu.click()

    def setCon(self):
        self.info.setText(self.cone)
    #metodos de teclado:

    def clicteclaUp(self):
        if self.mode == 'manual':
            valor_canon = self.angulo_canon.value()
            self.angulo_canon.setValue(valor_canon + 1)

    def clicteclaDown(self):
        if self.mode == 'manual':
            valor_canon = self.angulo_canon.value()
            self.angulo_canon.setValue(valor_canon - 1)
    
    def clicteclaRight(self):
        if  self.mode == 'manual':
            valor_base = self.angulo_base.value()
            self.angulo_base.setValue(valor_base + 1)

        elif self.mode == 'auto':
            valor_base = self.barra_base_auto.value()
            self.barra_base_auto.setValue(valor_base +1)
    
    def clicteclaLeft(self):
        if self.mode == 'manual':
            valor_base = self.angulo_base.value()
            self.angulo_base.setValue(valor_base - 1)

        elif self.mode == 'auto':
            valor_base = self.barra_base_auto.value()
            self.barra_base_auto.setValue(valor_base - 1)

    #primeros metrodos:
    def disparar(self):
        if self.mode=='manual' or self.mode == 'auto':
            receptionDate(0,0,'disp')
        else:
            print('ponga primero el modo')

    def recargar(self):
        if self.mode == 'None':
            print('ponga el modo')
        else:
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
        self.mode = 'manual'
        print(self.mode)

    def isclicAuto(self):
        self.manual_menu.setStyleSheet("background-color: rgb(23, 28, 47);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")
        self.automatic_menu.setStyleSheet("background-color: rgb(03, 08, 27);font: 700 9pt 'Tahoma';color: rgb(249, 255, 239);border-radius: 20px;")        
        self.mode = 'auto'
        print(self.mode)




def main():
    app = pyqt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()