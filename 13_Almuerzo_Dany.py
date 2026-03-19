#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#    MATEMÁTICA ALGORÍTMICA
#     MODELOS ESTOCÁSTICOS
#    ESFM IPN    MARZO 2026
#================================
#  Trabajo en clase. El almuezo de Dany es modelado por una CMTD.
#  El domingo, Dany elige al azar uniformemente, encuentre la probabilidad de que elija sushi el próximo miércoles y viernes, y pizza el sábado.
#================================
#  Como tal, nos pide lo siguiente: P(X_3 = 4, X_5 = 4, X_6 = 3)
#================================

import numpy as sp


#  MATRIZ Y VECTOR INICIAL

P = sp.matrix([[0.0, 0.5, 0.5, 0.0],
             [0.5, 0.0, 0.5, 0.0],
             [0.4, 0.0, 0.0, 0.6],
             [0.0, 0.2, 0.6, 0.2]])

comidas = ['Burrito', 'Falafel', 'Pizza', 'Sushi']

a = sp.matrix([0.25, 0.25, 0.25, 0.25])

#  CÁLCULO DE LAS MATRICES DE TRANSICIÓN DE 2 Y 3 PASOS

DP = P*P
TP = P*P*P

#  AHORA, TOMAMOS LOS VALORES QUE NECESITAMOS DE CADA UNA

aTP = a*TP
aTP4 = aTP[0, 3]

P_44 = DP[3, 3]
P_43 = P[3, 2]


#  FINALMENTE, MULTIPLICAMOS LOS DATOS OBTENIDOS

p = aTP4*P_44*P_43
print(f"La probabilidad deseada es: {p}")
