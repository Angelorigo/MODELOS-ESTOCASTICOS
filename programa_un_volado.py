#================================
#  ÁLVAREZ SERVÍN ÁNGEL RODRIGO
#================================
#     MATEMÁTICA ALGORÍTMICA     
#      MODELOS ESTOCÁSTICOS
#  ESFM IPN         FEBRERO 2026
#================================
#    SEGUNDO PROGRAMA VOLADO
#================================

import random

def lanzar_moneda():
    x = random.random()
    if 0 <= x <= 0.5:
        return "cara"
    else:
        return "cruz"

resultado = lanzar_moneda()
print(f"Resultado del tiro: {resultado}")
