import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def plot2DComplexidade(dfFB,dfPD,dfGUL,filename):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  X1 = dfFB['n']
  X2 = dfPD['n']
  X3 = dfGUL['n']
  Y1 = dfFB['C(n)']
  Y2 = dfPD['C(n)']
  Y3 = dfGUL['C(n)']

  # Plote as três funções em 3D usando plot_surface
  ax.plot(X1, Y1, label="FB")
  ax.plot(X2, Y2, label="OT")
  ax.plot(X3, Y3, label="GL")

  # Configuração dos rótulos dos eixos
  ax.set_xlabel('Quantidade de itens (n)')
  ax.set_ylabel(f'Quantidade de iterações')
  plt.legend()
  plt.savefig(filename)

  plt.show()
  
def plot2DComplexidade2(dfPD,dfGUL,filename):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  X2 = dfPD['n']
  X3 = dfGUL['n']
  Y2 = dfPD['C(n)']
  Y3 = dfGUL['C(n)']

  # Plote as três funções em 3D usando plot_surface
  ax.plot(X2, Y2, label="OT")
  ax.plot(X3, Y3, label="GL")

  # Configuração dos rótulos dos eixos
  ax.set_xlabel('Quantidade de itens (n)')
  ax.set_ylabel(f'Quantidade de iterações')
  plt.legend()
  plt.savefig(filename)

  plt.show()
  
def plot2DSolucao(dfFB,dfPD,dfGUL,filename):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  X1 = dfFB['n']
  X2 = dfPD['n']
  X3 = dfGUL['n']
  Y1 = dfFB['S(n)']
  Y2 = dfPD['S(n)']
  Y3 = dfGUL['S(n)']

  # Plote as três funções em 3D usando plot_surface
  ax.plot(X1, Y1, label="FB")
  ax.plot(X2, Y2, label="OT")
  ax.plot(X3, Y3, label="GL")

  # Configuração dos rótulos dos eixos
  ax.set_xlabel('Quantidade de itens (n)')
  ax.set_ylabel(f'Solução')
  plt.legend()
  plt.savefig(filename)

  plt.show()

df = pd.read_csv('csvs\\dados.csv')
dfFB =df[df['paradigma'] == 'FB']
dfGUL = df[df['paradigma'] == 'GUL']
dfOT = df[df['paradigma'] == 'OT']

print(df)
plot2DComplexidade(dfFB,dfOT,dfGUL,'imagens/complexidade.png')
plot2DComplexidade2(dfOT,dfGUL,'imagens/complexidade2.png')
plot2DSolucao(dfFB,dfOT,dfGUL,'imagens/solucao.png')
