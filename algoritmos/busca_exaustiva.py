from copy import deepcopy
import sys
def gerar_string_bits(n:int) -> str:
    return ["0" for i in range(n)] 

def somar_1_string_bits(string_bits:list, pos:int) -> None:
    if string_bits[pos] == "1":
        string_bits[pos] = "0"
        somar_1_string_bits(string_bits, pos-1)
    else:
        string_bits[pos] = "1"

    
def busca_exaustiva(elementos : list, n:int) -> (int,int):
    string_bits = gerar_string_bits(n) 
    min = 10**10
    execucoes = 0
    for i in range(2**(n-1)): 
        sum = 0
        for i in range(n):
            execucoes += 1 # Contagem para gráfico de complexidade 
            if string_bits[i] == "1":
                sum += elementos[i]
            else:
                sum -= elementos[i]
        sum = abs(sum)
        if sum < min:
            min = sum
        somar_1_string_bits(string_bits,n-1) 
    return min,execucoes
        
if __name__ == '__main__':
    elementos = [1,10,1]
    n = len(elementos)
    print(busca_exaustiva(elementos, n ))
    