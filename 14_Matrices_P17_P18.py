#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#    MATEMÁTICA ALGORÍTMICA
#     MODELOS ESTOCÁSTICOS
#    ESFM IPN    MARZO 2026
#================================
#  Trabajo en clase. Vemos el comportamiento de las matrices en 
#  su estado inicial, en las potencias 17 y 18, junto con sus
#  respectivos diagramas de transición.
#================================

import numpy as np
import sympy as sp
import networkx as nx
import matplotlib.pyplot as plt

#  Definimos las matrices: A, B, C, D; luego redondeamos los valores y los guardamos en una nueva matriz.

a = sp.Matrix([[0.2, 0.8],
              [0.6 ,0.4]])

b = sp.Matrix([[0.5, 0.4, 0.1, 0.0],
               [0.3, 0.3, 0.4, 0.0],
               [0.0, 0.0, 0.2, 0.8],
               [0.0, 0.0, 0.6, 0.4]])

c = sp.Matrix([[0.5, 0.4, 0.1, 0.0],
               [0.0, 1.0, 0.0, 0.0],
               [0.0, 0.0, 0.2, 0.8],
               [0.0, 0.0, 0.6, 0.4]])

d = sp.Matrix([[0.5, 0.4, 0.1, 0.0],
               [0.0, 0.0, 1.0, 0.0],
               [0.0, 0.2, 0.0, 0.8],
               [0.0, 0.0, 1.0, 0.0]])

A = a.applyfunc(lambda x: round(x, 4))
B = b.applyfunc(lambda x: round(x, 4))
C = c.applyfunc(lambda x: round(x, 4))
D = d.applyfunc(lambda x: round(x, 4))


#  Ahora calculamos las potencias 17 y 18, luego redondeamos los valores finales y los guardamos en una nueva matriz.

A17 = A**17
A18 = A**18
B17 = B**17
B18 = B**18
C17 = C**17
C18 = C**18
D17 = D**17
D18 = D**18

A7 = A17.applyfunc(lambda x: round(x, 4))
A8 = A18.applyfunc(lambda x: round(x, 4))
B7 = B17.applyfunc(lambda x: round(x, 4))
B8 = B18.applyfunc(lambda x: round(x, 4))
C7 = C17.applyfunc(lambda x: round(x, 4))
C8 = C18.applyfunc(lambda x: round(x, 4))
D7 = D17.applyfunc(lambda x: round(x, 4))
D8 = D18.applyfunc(lambda x: round(x, 4))

#  Seguimos con los respectivos diagramas de transición



#  Finalmente, imprimimos las matrices junto con sus respectivos diagramas de transición.

print("==============================================================\n")
print("  PROGRAMA MATRICES Y SU COMPORTAMIENTO EN GRANDES POTENCIAS\n")
print("==============================================================\n")
print("           Hola, las matrices iniciales son:\n")
print("\nA =")
sp.pprint(A, use_unicode=False)
print("\nB =")
sp.pprint(B, use_unicode=False)
print("\nC =")
sp.pprint(C, use_unicode=False)
print("\nD =")
sp.pprint(D, use_unicode=False)
print("\n==============================================================\n")
print("           Sigamos con la potencia 17\n")
print("\nA^17 =")
sp.pprint(A7, use_unicode=False)
print("\nB^17 =")
sp.pprint(B7, use_unicode=False)
print("\nC^17 =")
sp.pprint(C7, use_unicode=False)
print("\nD^17 =")
sp.pprint(D7, use_unicode=False)
print("\n==============================================================\n")
print("           Sigamos con la potencia 18\n")
print("\nA^18 =")
sp.pprint(A8, use_unicode=False)
print("\nB^18 =")
sp.pprint(B8, use_unicode=False)
print("\nC^18 =")
sp.pprint(C8, use_unicode=False)
print("\nD^18=")
sp.pprint(D8, use_unicode=False)
print("\n==============================================================\n")
