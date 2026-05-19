#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#     MATEMÁTICA ALGORÍTMICA
#      MODELOS ESTOCÁSTICOS
#     ESFM IPN     MAYO 2026
#================================
#  Hola, en este programa se ejecutarán
#  los 5 códigos para las distintas distribuciones
#  contenidas en la actividad 4.
#================================

import random as rnd
import numpy as np
import matplotlib.pyplot as plt


# =====================================================
# 1) WEIBULL We(alpha,1)
# =====================================================
def weibull(alpha, n):
    muestra = []
    for i in range(n):
        U = rnd.random()
        X = (-np.log(1-U))**(1/alpha)
        muestra.append(X)
    return muestra



# =====================================================
# 2) GUMBEL Gu(0,1)
# =====================================================

def gumbel(n):
    muestra = []
    for i in range(n):
        U = rnd.random()
        X = -np.log(-np.log(U))
        muestra.append(X)
    return muestra


# =====================================================
# 3) CAUCHY C(0,1)
# =====================================================
def cauchy(n):
    muestra = []
    for i in range(n):
        U = rnd.random()
        X = np.tan(np.pi*(U-0.5))
        muestra.append(X)
    return muestra


# =====================================================
# 4) LAPLACE L(0,1)
# =====================================================

def laplace(n):
    muestra = []
    for i in range(n):
        U = rnd.random()
        if U < 0.5:
            X = np.log(2*U)
        else:
            X = -np.log(2*(1-U))
        muestra.append(X)
    return muestra


# =====================================================
# 5) PARETO Par(alpha)
# =====================================================
def pareto(alpha, n):
    muestra = []
    for i in range(n):
        U = rnd.random()
        X = (1-U)**(-1/alpha)
        muestra.append(X)
    return muestra


#  PARÁMETROS
n = 1000
alpha = 2 
#  MUESTRAS
m_weibull = weibull(alpha, n)
m_gumbel = gumbel(n)
m_cauchy = cauchy(n)
m_laplace = laplace(n)
m_pareto = pareto(alpha, n)


# =====================================================
# HISTOGRAMA WEIBULL
# =====================================================

plt.figure(figsize=(7,5))
plt.hist(m_weibull, bins=40, density=True)
plt.title("Histograma Weibull")
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()


# =====================================================
# HISTOGRAMA GUMBEL
# =====================================================

plt.figure(figsize=(7,5))
plt.hist(m_gumbel, bins=40, density=True)
plt.title("Histograma Gumbel")
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()


# =====================================================
# HISTOGRAMA CAUCHY
# =====================================================

plt.figure(figsize=(7,5))
plt.hist(m_cauchy, bins=100, density=True)
plt.xlim(-10,10)
plt.title("Histograma Cauchy")
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()


# =====================================================
# HISTOGRAMA LAPLACE
# =====================================================

plt.figure(figsize=(7,5))
plt.hist(m_laplace, bins=40, density=True)
plt.title("Histograma Laplace")
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()


# =====================================================
# HISTOGRAMA PARETO
# =====================================================

plt.figure(figsize=(7,5))
plt.hist(m_pareto, bins=40, density=True)
plt.xlim(0,10)
plt.title("Histograma Pareto")
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()
