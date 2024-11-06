import serial
import time

connection = None

def conectar():
    global connection
    try:
        connection = serial.Serial(port='COM7', baudrate=115200, timeout=1)
        time.sleep(2)
        mess = 'Conexión hecha :)'
    except serial.SerialException as e:
        mess = f'No se pudo conectar :( - Error: {e}'
    return mess

def envio2esp(mensaje):
    try:
        if connection and connection.is_open:
            connection.write(mensaje.encode())
            mess = 'Envío correcto'
        else:
            mess = 'Conexión no está abierta'
    except serial.SerialException as e:
        mess = f'Fallo en el envío - Error: {e}'
        print(e)
    except AttributeError:
        mess = 'Conexión no establecida'
    return mess

def cerrar_conexion():
    global connection
    if connection and connection.is_open:
        connection.close()
