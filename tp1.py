import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# PARTE 1 -------------------------------

def distribucion_bernoulli(p, n=1, x=random.uniform(0, 1)): #1.1
    return p**x*(1-p)**(n-x)

def distribucion_binomial(p, n): #1-2
    return numero_combinatorio(n, 1) * distribucion_bernoulli(n, p, 1)

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def numero_combinatorio(n, x):
    return factorial(n)/factorial(x)*factorial(n - x)

def distribucion_exponencial(gamma): #1.3
    u = random.uniform(0, 1)
    return (-1/gamma) * (math.log(u))

def distribucion_normal(size): #1.4
    #Método Box-Muller
    #np.random.seed(521) #Numeros random predecibles (siempre son los mismos)

    u1 = np.random.uniform(size = 1000)
    u2 = np.random.uniform(size = 1000)
    R = np.sqrt(-2 * np.log(u1))
    print(R)
    Theta = 2 * np.pi * u2
    x = R * np.cos(Theta)
    y = R * np.sin(Theta)

    print(x)
    print(y)
    return x, y

# PARTE 2 --------------------------------------

def generar_numeros_exponenciales(): #2.1
    primerMuestra = []
    segundaMuestra = []
    terceraMuestra = []

    primerMuestra = generar_muestra_exponencial(10)
    segundaMuestra = generar_muestra_exponencial(30)
    terceraMuestra = generar_muestra_exponencial(100)

    media1 = calcular_media(primerMuestra)
    media2 = calcular_media(segundaMuestra)
    media3 = calcular_media(terceraMuestra)

    varianza1 = calcular_varianza(primerMuestra)
    varianza2 = calcular_varianza(segundaMuestra)
    varianza3 = calcular_varianza(terceraMuestra)

    print("Primer muestra (N=10): Media = " + str(media1) + " " + str(varianza1))
    print("Segunda muestra (N=30): Media = " + str(media2) + " " + str(varianza2))
    print("Tercera muestra (N=100): Media = " + str(media3) + " " + str(varianza3))

def generar_muestra_exponencial(n):
    muestra = []
    for i in range(n):
        muestra.append(distribucion_exponencial(0.5))
    return muestra

def calcular_media(lista):
    return sum(lista)/len(lista)

def calcular_varianza(lista):
    media = calcular_media(lista)
    varianza = sum((x-media)**2 for x in lista)/len(lista)
    return varianza

def generar_todos_los_histogramas(): #2.2
    muestra1 = generar_muestra_exponencial(10)
    muestra2 = generar_muestra_exponencial(30)
    muestra3 = generar_muestra_exponencial(100)

    generar_histograma(muestra1, 0.4)
    generar_histograma(muestra1, 0.2)
    generar_histograma(muestra1, 0.1)

    generar_histograma(muestra2, 0.4)
    generar_histograma(muestra2, 0.2)
    generar_histograma(muestra2, 0.1)
    
    generar_histograma(muestra3, 0.4)
    generar_histograma(muestra3, 0.2)
    generar_histograma(muestra3, 0.1)
    

def generar_histograma(muestra, ancho): 
    inicio = int(min(muestra))
    fin = int(max(muestra))
    n = int((fin-inicio)/ancho)
    res = stats.relfreq(muestra, n)
    x = res.lowerlimit + np.linspace(0, res.binsize*res.frequency.size, res.frequency.size)
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(x, res.frequency, width=res.binsize)
    ax.set_title('Muestras = ' + str(len(muestra)) + ", Ancho de banda = " + str(ancho))
    ax.set_xlim([x.min(), x.max()])
    plt.show()

generar_todos_los_histogramas()



