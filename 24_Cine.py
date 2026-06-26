#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#     MATEMÁTICA ALGORÍTMICA
#      MODELOS ESTOCÁSTICOS
#     ESFM IPN    JUNIO 2026
#================================
#  EXPOSICIÓN: SISTEMA DE LLEGADAS
#   Y SALIDAS DE LA DULCERÍA DEL
#              CINE.
#================================

import numpy as np
import matplotlib.pyplot as plt

#  Parámetros del sistema
num_clientes = 100

#  Promedio de llegada: 1 cliente cada 2 minutos
tasa_llegadas = 0.5

#  Promedio de atención: 1 cliente cada 1.5 minutos
tasa_servicio = 0.67

#  Generación de tiempos aleatorios
interarribos = np.random.exponential(1 / tasa_llegadas, num_clientes)
servicios = np.random.exponential(1 / tasa_servicio, num_clientes)

#  Tiempos de llegada
llegadas = np.cumsum(interarribos)

inicio_servicio = np.zeros(num_clientes)
fin_servicio = np.zeros(num_clientes)
esperas = np.zeros(num_clientes)

#  Simulación de la cola
for i in range(num_clientes):

    if i == 0:
        inicio_servicio[i] = llegadas[i]
    else:
        inicio_servicio[i] = max(llegadas[i], fin_servicio[i - 1])

    esperas[i] = inicio_servicio[i] - llegadas[i]
    fin_servicio[i] = inicio_servicio[i] + servicios[i]



#  Resultados
print("====================================================================")
print("           Hola, bienvenid@ al programa: DULCERÍA CINE")
print("====================================================================")
print(" -  Clientes atendidos:", num_clientes)
print(" -  Tiempo promedio de espera:", round(np.mean(esperas), 2), "minutos")
print(" -  Tiempo máximo de espera:", round(np.max(esperas), 2), "minutos")
print("====================================================================")

#  Gráfica
plt.plot(esperas)
plt.title("Tiempo de espera por cliente")
plt.xlabel("Cliente")
plt.ylabel("Minutos de espera")
plt.grid(True)
plt.show()
