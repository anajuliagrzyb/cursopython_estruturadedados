#Função 1 - O(n)
from timeit import timeit


def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

print(soma1(10))

