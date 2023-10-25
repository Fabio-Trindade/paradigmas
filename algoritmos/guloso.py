
from math import ceil, log

from numpy import argmax

from pd import pd


# def solucao_gulosa(elementos: list, n:int):
#     elementos = sorted(elementos, reverse=True)
#     sum = 0
#     execucoes = ceil(n*log(n,2))
#     for elemento in elementos:
#         execucoes += 1  # Contagem para gráfico de complexidade
#         sum = abs(sum - elemento)
#     return sum, execucoes

def solucao_gulosa(elementos: list, n:int):
    marcados =[False for i in range(n)]
    sum = 0
    execucoes = 0
    for i in range(n):
        min_diff = 10**10
        for j in range(n):
            execucoes += 1  # Contagem para gráfico de complexidade
            if not marcados[j] and abs(sum-elementos[j]) < min_diff:
                pos_min = j
                min_diff = abs(sum-elementos[j])
        marcados[pos_min] = True
        sum = abs(sum - elementos[pos_min])
    return sum, execucoes

if __name__ == '__main__':
    elementos = [30,14,23,2,1,4,3,432,3]
    n = len(elementos)
    print(solucao_gulosa(elementos, n ))
    print(pd(elementos, n ))
    
    
    # print(solucao_gulosa2(elementos, n ))