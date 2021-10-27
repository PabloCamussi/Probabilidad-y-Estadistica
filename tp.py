import random
import math

def distribucion_bernoulli(p, n=1, x=random.randint(0, 1)):
    return p**x*(1-p)**(n-x)

def distribucion_binomial(p, n):
    return numero_combinatorio(n, 1) * distribucion_bernoulli(n, p, 1)

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def numero_combinatorio(n, x):
    return factorial(n)/factorial(x)*factorial(n - x)

def distribucion_exponencial(λ):
    U = random.uniform(0, 1)
    return (-1/λ) * (math.log(U))

def distribucion_normal(μ, σ, x):
    #resultado = (1/math.sqrt(2*math.pi*σ**2)) * (2.71828**(-1*((x-μ)**2)/(2*σ**2)))
    resultado = (math.pi*σ) * math.exp(-0.5*((x-μ)/σ)**2)
    print(resultado)
    # Z = random.uniform(0, 1)
    # resultados = [Z * σ + μ for i in range(size)]
    # print

def distribucion_normal2(μ, σ, size=1):
    for i in range(size):
        Z = random.uniform(0, 1)
        resultado = Z * σ + μ
        if resultado < 5:
            print(resultado)

distribucion_normal(1, 2, 5)
