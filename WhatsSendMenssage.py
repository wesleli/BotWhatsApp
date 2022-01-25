import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import urllib

contatos_df = pd.read_csv("Enviar.csv", sep=';')
mensagem = open('Mensagem.txt', 'r', encoding='utf-8').read()


wd = webdriver.Chrome()
wd.get('https://web.whatsapp.com/')


def enviar():
    global cont_envios
    global sem_sucesso_datahora
    global sem_sucesso_indice
    global sem_sucesso_numero
    global contatos_df


    for i, numero in enumerate(contatos_df['Numero']):

            contato = str(numero)
            print(contato)
            texto = urllib.parse.quote(mensagem)

            try:

                link = f"https://web.whatsapp.com/send?phone={contato}&text={texto}"
                wd.get(link)
                while len(wd.find_elements(By.ID, "side")) < 1:
                    time.sleep(10)
                wd.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
                time.sleep(10)

                cont_envios += 1

            except:
                print('ocorreu um erro com o número:' + contato + 'indice:' + i)
                indice = i
                momento = datetime.datetime.today()
                sem_sucesso_numero.extend(contato)
                sem_sucesso_indice.extend(indice)
                sem_sucesso_datahora.extend[momento]




if __name__ == '__main__':

    cont_envios = 0
    begin = datetime.datetime.today()
    sem_sucesso_numero = []
    sem_sucesso_indice = []
    sem_sucesso_datahora = []

    while len(wd.find_elements(By.ID, "side")) < 1:
        time.sleep(5)

    enviar()

    wd.quit()
    end = datetime.datetime.today()

    dados = pd.DataFrame ({'Inicio': begin,
    'Enviados': cont_envios,
    'Indice Sem Sucesso de Envio': sem_sucesso_indice,
    'Numeros Sem Sucesso de Envio': sem_sucesso_numero,
    'Data e Hora Falha de Envio': sem_sucesso_datahora,
    'Fim': end
    })
    serie_log = str(begin)
    print(serie_log)
    serie_log = serie_log.replace(" ", "")
    print(serie_log)
    serie_log = serie_log.replace(":", "")
    print(serie_log)
    serie_log = serie_log.replace(".", "")
    print(serie_log)

    dados.to_csv('./logs/logUnfollow'+serie_log+'.csv')

    print('finalizado!')
    

    

    

    