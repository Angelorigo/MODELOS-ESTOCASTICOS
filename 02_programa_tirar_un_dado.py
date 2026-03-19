#================================
#  ÁLVAREZ SERVÍN ÁNGEL RODRIGO
#================================
#     MATEMÁTICA ALGORÍTMICA     
#      MODELOS ESTOCÁSTICOS
#  ESFM IPN         FEBRERO 2026
#================================
#   PROGRAMA DE SIMULACIÓN DEL
#     LANZAMIENTO DE UN DADO
#================================

import random

def lanzar_dado():
    resultado = random.randint(1, 6)
    return resultado

print(f"Resultado del dado: {lanzar_dado()}")
