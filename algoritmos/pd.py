# from algoritmos.busca_exaustiva import busca_exaustiva


def pd(elementos: list, n:int ):
    sum = 0
    execucoes = 0
    for i in range(n):
        sum += elementos[i]
    temp = sum
    sum = int(sum/2)
    F=[[None]*(sum+1) for i in range(n + 1)]
    
    for i in range(n+1):
        F[i][0] = True
        
    for i in range(1,sum+1):
        F[0][i] = False
        
    for i in range(1,n+1):
        for j in range(1,sum+1):
            execucoes += 1  # Contagem para gráfico de complexidade
            if elementos[i-1] <= j:
                F[i][j] = F[i-1][j] or  F[i - 1][j - elementos[i - 1]]
            else:
                F[i][j] = F[i - 1][j]
    for i in range(sum,-1,-1):
        if (F[n][i] == True):
            min = temp - 2*i
            break
        
    return min, execucoes

if __name__ == '__main__':
    elementos = [5,6,2,30,7]
    n = len(elementos)
    # print(busca_exaustiva(elementos, n ))
    print(pd(elementos, n ))