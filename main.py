import sys
import PyQt5.QtWidgets as pyqt
from PyQt5 import uic

class Principal(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
    
    def initGUI(self):
        uic.loadUi('canon_interfaz.ui',self)
        self.automatic_menu.clicked.connect(lambda: self.funcion())
        self.angulo_base()#borarr
        self.show()
    
    def funcion(self):
        print('hola')

    def canon_angulo(self): # ejemplo
        pass
    
    def angulo_base(self):
        print(self.horizontalSlider_3.value())

def main():
    app = pyqt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()