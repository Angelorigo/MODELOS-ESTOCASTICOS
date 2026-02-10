#================================
#  ÁLVAREZ SERVÍN ÁNGEL RODRIGO
#================================
#     MATEMÁTICA ALGORÍTMICA     
#      MODELOS ESTOCÁSTICOS
#  ESFM IPN         FEBRERO 2026
#================================
#PRIMER PROGRAMA: Tenemos un tablero circular de 4 secciones (azul, naranja, rojo, verde), dos monedas y una ficha o token. El juego funciona así: se lanzan las dos monedas y se avanza el número de caras obtenidas.
#  ESTE PROGRAMA GRAFICA N TIRADAS PARA LOS JUEGOS INICIADOS EN CUALQUIER COLOR
#================================

import numpy as np
import matplotlib.pyplot as plt

#  Definimos la matriz de transición A
#  Las columnas representan el color actual y las filas el siguiente:
#  [Azul, Naranja, Rojo, Verde]
A = np.array([
    [0.25, 0.00, 0.25, 0.50], # Probabilidad de caer en Azul
    [0.50, 0.25, 0.00, 0.25], # Probabilidad de caer en Naranja
    [0.25, 0.50, 0.25, 0.00], # Probabilidad de caer en Rojo
    [0.00, 0.25, 0.50, 0.25]  # Probabilidad de caer en Verde
])

#  Ahora elegimos el vector inicial X_0
#  Digamos que la ficha empieza en Azul, luego guardemos el historial para 25 tiradas
X = np.array([1.0, 0.0, 0.0, 0.0])
n_tiradas = 15
historial = [X]

#  Sustituimos en el sistema X_n = A * X_n-1
for n in range(n_tiradas):
    X = np.dot(A, X) 
    historial.append(X)

historial = np.array(historial)

#  GRAFICACIÓN
plt.figure(figsize=(10, 6))
colores = ['blue', 'orange', 'red', 'green']
nombres = ['Azul', 'Naranja', 'Rojo', 'Verde']

for i in range(4):
    plt.plot(historial[:, i], label=nombres[i], color=colores[i], marker='o', markersize=4)

plt.title('Cambio de probabilidad en el límite')
plt.xlabel('Número de tiradas (n)')
plt.ylabel('Probabilidad P(Xn)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
