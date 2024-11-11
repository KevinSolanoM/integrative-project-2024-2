import serial
import time


connection = None

def conectar():
    global connection
    if connection and connection.is_open:
        return 'Conexión ya está activa.'
    try:
        connection = serial.Serial(port='COM7', baudrate=115200, timeout=1)
        time.sleep(1)  # Asegúrate de que la conexión esté establecida
        return 'Conexión hecha :)'
    except serial.SerialException as e:
        return f'No se pudo conectar :( - Error: {e}'

def envio2esp(mensaje):
    try:
        if connection and connection.is_open:
            time.sleep(0.1)
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

def datosFromEsp():
    try:
        datos = connection.readline().decode('utf-8')
        datolim = datos.strip()
        time.sleep(0.1)
        return datolim
        #print('angulo pot: ',datolim)

    except:
        print('no se pudo conectar')

def cerrar_conexion():
    global connection
    if connection and connection.is_open:
        connection.close()
        print("Conexión cerrada")
