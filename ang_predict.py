import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt



##cambiar los datos!!! 
datos = [
    (10,200), (20, 248), (40, 290), (60, 150)
]

def prediction(dis: float = None):

    angulos = np.array([x[0] for x in datos]).reshape(-1, 1) 
    distancias = np.array([x[1] for x in datos])




    grado = 4
    modelo = make_pipeline(PolynomialFeatures(grado), LinearRegression())
    modelo.fit(angulos, distancias) 


    if dis is None:
        angulos_nuevos = np.linspace(0, 90, 100).reshape(-1, 1) 
        distancias_pred = modelo.predict(angulos_nuevos) 
        return distancias_pred, angulos_nuevos  
    else:


        modelo_invertido = make_pipeline(PolynomialFeatures(grado), LinearRegression())
        modelo_invertido.fit(distancias.reshape(-1, 1), angulos)  

        angulo_predic = modelo_invertido.predict(np.array([dis]).reshape(-1, 1)) 
        return angulo_predic[0]  

def prediccionesGraficas():

    dista_pred, angulos_nuevos = prediction()


    angulos_originales = np.array([x[0] for x in datos])
    distancias_originales = np.array([x[1] for x in datos])
    plt.plot(angulos_originales, distancias_originales, 'bo', label='Datos reales') 


    #
    plt.plot(angulos_nuevos, dista_pred, 'r-', label='Predicción') 

    plt.legend()  
    plt.xlabel('Ángulo (°)')
    plt.ylabel('Distancia en (cm)')
    plt.title('Gráfica de Datos Reales vs Predicciones')
    plt.show() 

