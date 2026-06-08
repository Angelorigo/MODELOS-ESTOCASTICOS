#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#     MATEMÁTICA ALGORÍTMICA
#      MODELOS ESTOCÁSTICOS
#     ESFM IPN    JUNIO 2026
#================================
#  Simulación de un movimiento Browniano discretizado 
#  hecha en clase, Junio-08-2026
#================================

import matplotlib.pyplot as plt
import numpy as np
import random as rd

def sim(T, L):
    dt = T/L
    W0 = 0
    Wi_1 = [W0]
    for i in range(L-1):
        xi = rd.normalvariate(0,1)
        W0 += np.sqrt(dt)*xi
        Wi_1.append(W0)
    return Wi_1

L = sim(100,1000)
plt.plot(L)
plt.show()
