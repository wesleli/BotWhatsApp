
from os import sep
import pandas as pd

contatos_df = pd.read_csv('Enviar.csv', sep=';')
contatos = []

for i, numero in enumerate(contatos_df['Numero']):
    contato = (i, numero)
    contatos.extend(contato)
    print(contato)


sem_sucesso_contato = []

sem_sucesso_contato.extend(contatos)

print(sem_sucesso_contato)