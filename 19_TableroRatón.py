#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#     MATEMÁTICA ALGORÍTMICA
#      MODELOS ESTOCÁSTICOS
#     ESFM IPN     MAYO 2026
#================================
#  Este programa simula el tablero del ratón con queso y shock
#  Vamos a ver el programa, teniendo en cuenta que inicia en la casilla 0
#================================

import sympy as sp

a = sp.Rational(1, 2)
b = sp.Rational(1, 3)
c = sp.Rational(1, 4)

M = sp.Matrix([
    [0, a, a, 0, 0, 0, 0, 0, 0], # 0
    [b, 0, 0, b, 0, 0, 0, b, 0], # 1
    [b, 0, 0, b, 0, 0, 0, 0, b], # 2
    [0, c, c, 0, c, c, 0, 0, 0], # 3
    [0, 0, 0, b, 0, 0, b, b, 0], # 4
    [0, 0, 0, b, 0, 0, b, 0, b], # 5
    [0, 0, 0, 0, a, a, 0, 0, 0], # 6
    [0, 0, 0, 0, 0, 0, 0, 1, 0], # 7 Comida
    [0, 0, 0, 0, 0, 0, 0, 0, 1]  # 8 Schock
])

#==========================================================
#  CÁLCULO DE PROBABILIDADES DE ABSORCIÓN
#==========================================================

#  Matriz Q
Q = M[0:7, 0:7]

#  Matriz R
R = M[0:7, 7:9]

#  Matriz Identidad 
I = sp.eye(7)

#  Matriz Fundamental N = (I - Q)^-1
N = (I - Q).inv()

#  Matriz de probabilidades de absorción B = N * R
B = N * R


prob_comida = B[0, 0]
prob_toque = B[0, 1]

print("========================================================\n")
print("   RESULTADOS DEL RATONCITO:\n")
print(f"Probabilidad de llegar a la comida (casilla 7): {prob_comida}")
print(f"Probabilidad de llegar al toque  (casilla 8): {prob_toque}")
print("\n========================================================\n")
