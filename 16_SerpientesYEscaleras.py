#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#     MATEMÁTICA ALGORÍTMICA
#      MODELOS ESTOCÁSTICOS
#     ESFM IPN     MAYO 2026
#================================
#  ACTUALIZACIÓN DEL PROGRAMA:
#  Matriz de transición del tablero serpientes y escaleras 
#  propuesto en clase. Solución por simulación a las 
#  preguntas propuestas en clase.
#================================


import sympy as sp


#  Definimos las probabilidades exactas con fracciones

a = sp.Rational(1, 6)
b = sp.Rational(1, 5)
c = sp.Rational(1, 3)
d = sp.Rational(1, 2)


#  Definimos la matriz completa entrada por entrada

M = sp.Matrix([
    [0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, b, b, b, b],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [c, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, c, c],
    [d, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


#  Imprimimos la matriz de transición

print("=========================================================================================================\n")
print("                                        SERPIENTES Y ESCALERAS:\n\n")
print("M = \n")
sp.pprint(M, use_unicode = False)
print("\n=========================================================================================================\n")


#=======================================================================
#  CÁLCULO DEL NÚMERO PROMEDIO DE TIRADAS (CADENAS ABSORBENTES)
#=======================================================================

#  Hacemos una copia para no alterar la original

M_juego = M.copy()


#  Convertimos la casilla 20 en un estado absorbente (el juego termina ahí)

for j in range(21):
    M_juego[20, j] = 1 if j == 20 else 0


# 3. Extraemos la submatriz Q (estados del 0 al 19)

Q = M_juego[0:20, 0:20]


# 4. Creamos la matriz Identidad (I) de 20x20

I = sp.eye(20)


# 5. Calculamos la matriz fundamental N = (I - Q)^(-1)

N = (I - Q).inv()


# 6. Sumamos la primera fila de N para obtener el promedio de tiradas desde el inicio

pasos_esperados_exactos = sum(N[0, :])
pasos_esperados_decimal = float(pasos_esperados_exactos)


# Imprimimos los resultados
print("\n=========================================================================================================\n")
print("  - ¿Cuál es el número promedio de tiradas necesarias para terminar el juego?\n")
print(f"   + Respuesta exacta: {pasos_esperados_exactos} tiradas.")
print(f"   + Respuesta en decimal: {pasos_esperados_decimal:.4f} tiradas.")
print("\n=========================================================================================================\n")
