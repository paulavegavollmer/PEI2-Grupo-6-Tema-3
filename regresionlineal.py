import numpy as np
import matplotlib.pyplot as plt
x = voltaje_sensor = np.array([0.0, 1.25, 2.45, 3.80, 5.10])
y = fuerza_real = np.array([0.0, 15.2, 31.0, 48.5, 65.3])
# plt.scatter(x, y, color = "red", label='Datos experimentales') #Hacer una grafica de puntos con los datos experimentales
# plt.xlabel('Voltaje [V]') #Llamar al eje x "Voltaje [V]"
# plt.ylabel('Fuerza [kN]') #Llamar al eje y "Fuerza [kN]"
# plt.title('Calibración del sensor de empuje') #Poner un título al gráfico
# plt.legend() #Enseñar la leyenda
# plt.grid(True) #Activar la cuadrícula, tambien vale si pones plt.grid() sin argumentos
#plt.show() #Mostrar el gráfico

m_c = np.polyfit(x, y, 1) #Ajuste lineal de los datos experimentales, de grado del polinomio 1 (recta), coeficientes = np.array([m_c])
#print(m_c) #Imprimir los coeficientes de la recta
xn = np.linspace(0, 5.5, 10) #Generar 100 puntos entre 0 y 5.5 para la recta de ajuste
yn = np.polyval(m_c, xn) #Evaluar la recta de ajuste en los puntos generados
plt.scatter(x, y, color = "red", label='Datos experimentales') #Hacer una grafica de puntos con los datos experimentales
plt.xlabel('Voltaje [V]') #Llamar al eje x "Voltaje [V]"
plt.ylabel('Fuerza [kN]') #Llamar al eje y "Fuerza [kN]"
plt.title('Calibración del sensor de empuje') #Poner un título al gráfico
plt.plot(xn, yn, color = "blue", label='Ajuste lineal') #Hacer una grafica de la recta de ajuste
plt.legend() #Enseñar la leyenda
plt.grid(True) #Activar la cuadrícula
plt.show() #Mostrar el gráfico

from sistemalineal import my_Gauss
from numpy import array, transpose, matmul
def my_linear_regression(a,b):
    A_transposed = array([a**n for n in range(2)])
    A = transpose(A_transposed)
    matriz_tranformada = matmul(A_transposed, A)
    vector_tranformado = matmul(A_transposed, b)
    resultados = my_Gauss(matriz_tranformada, vector_tranformado)
    ecuación = f"F= {resultados[1]}*V +{resultados[0]}"
    return ecuación
# falta redondear resultados, quizás a 2 decimales, salen demasiados (creo que 16)
# para formar la ecuación, se usa la f""" para crear una función y se llama a los coeficientes entre llaves
