import serial
import time



def conectar():
    global connection
    try:
        connection = serial.Serial(port='COM8',baudrate= 115200)
        time.sleep(2)
        
        mess = ('conección hecha  :)')
    except:
        
        mess = ('no se puedo conectar :(')
    return mess
    
def envio2esp(mensaje):
    try:
        connection.write(mensaje.encode())
    except:
        
        mess = ('algo a fallado')

    return mess
