#================================
#  ÁLVAREZ SERVÍN ÁNGEL RODRIGO
#================================
#      MODELOS ESTOCÁSTICOS
#  ESFM IPN         FEBRERO 2026
#================================
# PROGRAMA N TIROS, GRAFICACIÓN
#    Y CÁLCULO DE PROBABILIDAD 
#        USANDO P ^ Q=1-P
#================================

import random
import matplotlib.pyplot as plt

print("Ingrese el valor de P entre 0 y 1 para que de un salto a la derecha:")
P = float(input())

def simulacion_n_tiros(n):
    posicion = 0                 
    posiciones = [posicion]       
    derechas = 0

    for i in range(1, n + 1):
        x = random.random()
        if x <= P:
            posicion += 1       
            derechas += 1
        else:
            posicion -= 1         

        posiciones.append(posicion)

    izquierdas = n - derechas

    print(f"Resultados tras {n} tiros:")
    print(f"Saltos a la derecha: {derechas} (Probabilidad: {derechas/n:.4f})")
    print(f"Saltos a la izquierda: {izquierdas} (Probabilidad: {izquierdas/n:.4f})")
    
    if {posicion} == 0:
        print(f"Se regreso al origen")
    else:
        print(f"se alejo {posicion} unidades del origen")

    plt.figure(figsize=(10, 5))
    plt.plot(range(n + 1), posiciones, linewidth=1)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.xlabel("Número de pasos")
    plt.ylabel("Posición en ℤ")
    plt.title("Caminata aleatoria en la recta de los enteros")
    plt.grid(True)
    plt.show()

simulacion_n_tiros(1000)
