#================================
#  ÁLVAREZ SERVÍN ÁNGEL RODRIGO
#================================
#     MATEMÁTICA ALGORÍTMICA
#      MODELOS ESTOCÁSTICOS
#  ESFM IPN         MARZO 2026
#================================
#  Dada una distribución inicial, y la matriz de transición P,  basado en el juego del tablero de 4 colores
#       Grafica N pasos
#================================
#  Se pidió que fuera con 100 pasos pero las probabilidades acumuladas tienden a 0 y no se visualiza bien la gráfica, así que lo cambié a 20, en caso de querer graficar los 100 pasos, cambie el valor de n en la línea 28
#================================

import random
import numpy as np
import matplotlib.pyplot as plt


# [Azul, Naranja, Rojo, Verde]
colores = ['A', 'N', 'R', 'V']


#  Se pide al usuario llenar la matriz de 4x4, y posteriormente dar el vector de distribución inicial

print(f"===========================================================================")
print("CAMINATA ALEATORIA EN EL TABLERO: Azul, Naranja, Rojo, Verde.\n")
print("Por favor, ingrese los valores deseados para la matriz de transición de 4x4")
print("de tal manera que sumados, den 1; separado por comas (ej, 0.5 0.0 0.4 0.1)")

P_lista = []
for i in range(4):
    entrada_fila = input(f"Probabiidades de salto desde {colores[i]}: ")
    fila = [float(x) for x in entrada_fila.split()]
    P_lista.append(fila)
P = np.array(P_lista)
n = 100
print(f"===========================================================================")
print("Ahora, ingrese el vector de distribución inicial de 1x4, separado por comas y que sumen 1.")
entrada_a = input("VECTOR INICIAL: ")
a = np.array([float(x) for x in entrada_a.split()])


#  Aquí se muestra al usuario el vector de valores iniciales para los estados, junto con la matriz de transición dada.

print(f"===========================================================================")
print(f"                 Tu vector de valores iniciales es:")
print(f"                       {a}")
print(f"===========================================================================")
print(f"                    Tu matriz de transición es:")
print(f"{P}")
print(f"===========================================================================")
print(f"    Considere: A = Azul, N = Naranja, R = Rojo, V = Verde")


X = []  # X Guarda el camino


#  Usamos la librería random para escoger entre los 4 colores

X_0 = np.random.choice([0, 1, 2, 3], p = a)
X.append(X_0)


#  Cálculo de la probabilidad acumulada, iniciando en X_0

PA = a[X_0]


#  Bucle

print(f"---------------------------------------------------------------------------")
for i in range (1, n+1):
    j = X[i-1]
    p = P[j, :]
    X_i = np.random.choice([0, 1, 2, 3], p=p)
    X.append(X_i)
    PA *= P[j, X_i]
    print(f"{i}, de {colores[j]}, a {colores[X_i]}; Con probabilidad: {P[j, X_i]}")
    print(f"---------------------------------------------------------------------------")

camino = [colores[estado] for estado in X]


#  IMPRESIÓN DE RESULTADOS

print(f"\n===========================================================================") 
print(f"La trayectoria fue:\n{' -> '.join(camino)}")
print(f"===========================================================================")
print(f"Probabilidad de llegar a este evento, dado el camino anterior: {PA:.20f}")
print(f"===========================================================================")


#  Cuántas veces estuvo el valor en cada color del tablero?

print("---------------------------------------------------------------------------")
print("PORCENTAJES:\n")
for i in range(4):
    visita = X.count(i)
    porcentaje = (visita / len(X)) * 100
    print(f"{colores[i]}: Cayó {visita} veces ({porcentaje:.2f}%)")
print("---------------------------------------------------------------------------")

#  GRAFICACIÓN

plt.figure(figsize=(10, 5))
plt.step(range(n+1), X, where = 'post', marker = 'o', color = 'crimson', linewidth = 2)
plt.yticks([0, 1, 2, 3], colores)
plt.xlabel("Número de pasos")
plt.ylabel("Posición en el tablero")
plt.title("TABLERO CAMINATA ALEATORIA")
plt.grid(True)
plt.show()
