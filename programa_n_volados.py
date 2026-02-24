#================================
#  ÁLVAREZ SERVÍN ÁNGEL RODRIGO
#================================
#      MODELOS ESTOCÁSTICOS
#  ESFM IPN         FEBRERO 2026
#================================
# PROGRAMA N VOLADOS, GRAFICACIÓN
#    Y CÁLCULO DE PROBABILIDAD 
#================================

import random
import matplotlib.pyplot as plt

def simulacion_n_tiros(n):
    caras = 0
    prob_cara_acumulada = []
    tiros = []

    for i in range(1, n + 1):
        x = random.random()
        if x <= 0.5:
            caras += 1

        prob_cara = caras / i
        prob_cara_acumulada.append(prob_cara)
        tiros.append(i)

    cruces = n - caras
    print(f"Resultados tras {n} lanzamientos:")
    print(f"Caras: {caras} (Probabilidad: {caras/n:.4f})")
    print(f"Cruces: {cruces} (Probabilidad: {cruces/n:.4f})")

    plt.plot(tiros, prob_cara_acumulada, label="Probabilidad empírica de cara")
    plt.axhline(0.5, linestyle="--", label="Probabilidad teórica = 0.5")
    plt.xlabel("Número de lanzamientos")
    plt.ylabel("Probabilidad acumulada")
    plt.title("Estabilización de la probabilidad al lanzar una moneda")
    plt.legend()
    plt.grid(True)
    plt.show()

simulacion_n_tiros(1000)
