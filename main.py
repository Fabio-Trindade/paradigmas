import csv
from random import randint
from algoritmos.busca_exaustiva import busca_exaustiva
from algoritmos.pd import pd
from algoritmos.guloso import solucao_gulosa

with open('csvs/dados.csv',mode='w',encoding='utf-8',newline='') as nome_arquivo:
    file_csv = csv.writer(nome_arquivo,delimiter=',')
    file_csv.writerow(['n','C(n)','S(n)','paradigma'])
    for i in range(1,25+1):
        print(i)
        elementos = [randint(0,i) for j in range(i)]
        n = i
        sol_gul, execucoes_gul = solucao_gulosa(elementos, n )
        solucao_pd, execucoes_pd = pd(elementos, n )
        solucao_fb, execucoes_fb = busca_exaustiva(elementos, n )
        assert(solucao_pd == solucao_fb)
        dados = [(solucao_fb,execucoes_fb,"FB"),(sol_gul,execucoes_gul,"GUL"),(solucao_pd,execucoes_pd,"OT")]
        for sol,exec,paradigma in dados:
            file_csv.writerow([str(n),str(exec),str(sol),paradigma]) 