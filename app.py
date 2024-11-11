import PyQt5.QtWidgets as pyqt
from PyQt5 import uic
import sys
from PyQt5.QtGui import QPixmap
from connect2bt import conectar
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import time
from connect2bt import datosFromEsp
from PyQt5.QtCore import QTimer
from ang_predict import prediccionesGraficas, prediction

from calculator_ang import receptionDate

conectar()

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
        self.velocidad_canon.valueChanged.connect(lambda: self.ajustarManual())

        #disparar:

        self.disparar_auto.clicked.connect(lambda: self.disparar())
        self.disparar_manual.clicked.connect(lambda: self.disparar())

        #recargar:
        self.recarga_manual.clicked.connect(lambda: self.gatillo())

        self.recoger.clicked.connect(lambda: self.recargar(2))
        self.soltar.clicked.connect(lambda: self.recargar(1))


        pixmap = QPixmap("images\logodragon.png")
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True) 

        self.image2.setPixmap(pixmap)
        self.image2.setScaledContents(True)

        #atajos de teclado

        self.shortcut_a = pyqt.QShortcut(QKeySequence(Qt.Key_A), self)
        self.shortcut_a.activated.connect(self.recoger.click)
        
        self.shortcut_d = pyqt.QShortcut(QKeySequence(Qt.Key_D), self)
        self.shortcut_d.activated.connect(self.soltar.click)

        self.shortcut_up = pyqt.QShortcut(QKeySequence(Qt.Key_Up), self)
        self.shortcut_up.activated.connect(self.clicteclaUp)

        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Down), self)
        self.shortcut_down.activated.connect(self.clicteclaDown)
        
        self.shortcut_up = pyqt.QShortcut(QKeySequence(Qt.Key_Left), self)
        self.shortcut_up.activated.connect(self.clicteclaLeft)
        
        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Right), self)
        self.shortcut_down.activated.connect(self.clicteclaRight)



        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut_down.activated.connect(lambda: self.disparar())
        
        self.shortcut_down = pyqt.QShortcut(QKeySequence(Qt.Key_Tab), self)
        self.shortcut_down.activated.connect(self.chageMode)

        self.shortcut_Space = pyqt.QShortcut(QKeySequence(Qt.Key_Space), self)
        self.shortcut_Space.activated.connect(self.recarga_manual.click)



        self.objetivo.valueChanged.connect(lambda: self.predDisManaul())
        self.objetivo_2.valueChanged.connect(lambda: self.predDisAuto())

        #ejecucion continua del el cambio del texto


        #plot:
        self.open_plot.clicked.connect(prediccionesGraficas)

        #otro intengo del potenciometro
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mostrar_datos)
        self.timer.start(10)

        self.show()

    
    def predDisManaul(self):
        val = int(self.objetivo.value())
        ang_predi= round(((prediction(val))[0]),2)
        self.valor_recomendado.setText(str(ang_predi)+'°')

    def predDisAuto(self):
        val = int(self.objetivo_2.value())
        ang_predi= round(((prediction(val))[0]),2)
        print(val)
        print(ang_predi)
        self.valor_recomendado_2.setText(str(ang_predi)+'°')

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
            valor_canon = self.velocidad_canon.value()
            self.velocidad_canon.setValue(valor_canon + 15)

    def clicteclaDown(self):
        if self.mode == 'manual':
            valor_canon = self.velocidad_canon.value()
            self.velocidad_canon.setValue(valor_canon - 15)
            
    
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
    def gatillo(self):
        if self.mode=='manual' or self.mode == 'auto':
            receptionDate(0,0,'rec_gat')
        else:
            print('ponga primero el modo')

    def recargar(self,ifgiro:int):
        if self.mode == 'None':
            print('ponga el modo')
        else:
            if ifgiro==None:
                receptionDate(0,0,'rec')
            elif ifgiro==1:
                receptionDate(0,1,'rec1')
            elif ifgiro==2:
                receptionDate(0,2,'rec1')
            else:
                print('¿error?:/')

    def ajustarAuto(self):
        base_ang = self.barra_base_auto.value()
        distancia = self.distancia_auto.value()
        receptionDate(base_ang,distancia,'auto')
        self.recargar(None)

    def ajustarManual(self):
        base_ang = self.angulo_base.value()
        canon_ang = self.velocidad_canon.value()
        receptionDate(base_ang,canon_ang,'manual')
    
    def mostrar_datos(self):
        data = datosFromEsp()
        self.text_angulo.setText(data)
        self.text_angulo_2.setText(data)
        #datos a mostrar desde la esp
        #datos = datosFromEsp()
        #if datos:
        """""
            base_actual = datos[0:3]
            canon_actual = datos[3:5]

            self.text_base.setText(base_actual)
            self.text_angulo.setText(canon_actual)
            
            self.text_base_2.setText(base_actual)
            self.text_angulo_2.setText(canon_actual)"""
            


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