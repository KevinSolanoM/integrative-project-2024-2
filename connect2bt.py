import serial
import time
def conectar():
    global connection
    try:
        connection = serial.Serial(port='COM8',baudrate= 115200)
        time.sleep(2)
        print('coneccion hecha  :)')
    except:
        print('no se puedo conectar :(')
    
    
def envio2esp(mensaje):
    try:
        connection.write(mensaje.encode())
    except:
        print('algo a fallado')
