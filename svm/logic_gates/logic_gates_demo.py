# Bibiotecas para análise
import pandas as pd
import numpy as np
from sklearn import svm
# Bibliotecas para visulização dos dados
import matplotlib as ptl
import seaborn as sns

sns.set(font_scale=1.2)

# Importar os dados

portas = pd.read_csv('logic_gates.csv')

# Preparar os dados

entradas = portas[['E1', 'E2', 'S']].values

marcacoes = np.where(portas['Type'] == 'and', 0, 1)

# Treinar o modelo

modelo = svm.SVC(kernel='linear')
modelo.fit(entradas, marcacoes)


# Função para prever um novo caso

def and_or(E1, E2, S):
    if modelo.predict([[E1, E2, S]]) == 0:
        print("É uma porta AND!")
    else:
        print("É uma porta OR!")


# Prevendo um novo caso

and_or(1, 0, 0)

and_or(1, 0, 1)
