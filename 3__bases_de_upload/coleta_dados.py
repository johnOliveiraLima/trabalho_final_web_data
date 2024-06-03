import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.common.exceptions import NoSuchElementException

navegador = webdriver.Chrome()
navegador.get('https://m.imdb.com/chart/toptv/?ref_=nv_tvv_250')

xpaths = [
    #  0 - Título:
    '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/a/h3',
    # 1 - Estréia e final:
    '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[1]',
    # 2 - Número de episódios:
    '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[2]',
    # 3 - Classificação indicativa:
    '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[3]',
    # 4 - Notas:
    '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/span/div/span',
    # 5 - Número de Avaliações
    '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/span/div/span/span'
]

# O terceiro indice é o que muda
titulo1 = navegador.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[1]/a/h3').text
titulo2 = navegador.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div[2]/div/div/div[1]/a/h3').text
titulo3 = navegador.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[3]/div[2]/div/div/div[1]/a/h3').text
print(titulo1)
print(titulo2)
print(titulo3)

def separa_ano(titulo, separador):
    ano = []
    duracao = titulo.split(separador)
    ano.append(duracao[0])
    if len(duracao) < 2:
        ano.append(duracao[0:4])
        return ano
    else:
        return duracao[0:4]
    
def separa_nome(titulo, separador):
    ano = []
    duracao = titulo.split(separador)
    ano.append(duracao)
    if len(duracao) < 2:
        ano.append(duracao)
        return ano
    else:
        return duracao
    
def valor_limpo(xpath, separador, index):
    return separa_nome(navegador.find_element(By.XPATH,xpath).text,separador)[index]

def valor_limpo_ano(xpath, separador, index):
    return separa_ano(navegador.find_element(By.XPATH,xpath).text,separador)[index]

periodo = navegador.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[3]/div[2]/div/div/div[2]/span[1]').text
separa_ano(periodo,'–')

def nota_filme(xpath):
    nota = navegador.find_element(By.XPATH,xpath).text
    return nota[0:3]

def num_ava(xpath):   
    n_avaliacoes = navegador.find_element(By.XPATH,xpath).text
    return n_avaliacoes.strip()[1:-1]

def coleta_classificacao(xpath):
    try:
        classif = navegador.find_element(By.XPATH,xpath).text
        return classif
    except NoSuchElementException:
        return None

numero_eps = valor_limpo('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[2]',' ',0)
numero_eps

estreia = valor_limpo('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[1]','–',0)
estreia

estreia = separa_nome(navegador.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[1]').text,'–')[0]
estreia

final = separa_nome(periodo,'–')[1]
final

final = valor_limpo('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[1]','–',1)
final

final = separa_nome(navegador.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div[2]/div/div/div[2]/span[1]').text,'–')[1]
final

titulos = []
estreias = []
finais = []
numeros_eps = []
classificacoes = []
notas = []
num_avaliacoes = []
for i in range(1,101):
    titulos.append(valor_limpo('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[1]/a/h3','. ', 1))
    estreias.append(valor_limpo_ano('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[2]/span[1]','–',0))
    finais.append(valor_limpo_ano('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[2]/span[1]','–',1))
    numeros_eps.append(valor_limpo('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[2]/span[2]',' ',0))
    classificacoes.append(coleta_classificacao('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[2]/span[3]'))
    notas.append(nota_filme('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/span/div/span'))
    num_avaliacoes.append(num_ava('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/span/div/span/span'))

tabela = []
tabela.append(titulos)
tabela.append(estreias)
tabela.append(finais)
tabela.append(numeros_eps)
tabela.append(classificacoes)
tabela.append(notas)
tabela.append(num_avaliacoes)

df = pd.DataFrame(tabela).T
df = df.rename(columns={
    0:'Título',
    1:'Estréia',
    2:'Final',
    3:'Nº episódios',
    4:'Classificação',
    5:'Nota',
    6:'Nº avaliações'
}
)
def converte_lista(valor):
    if isinstance(valor,list):
        return valor[0] if len(valor) > 0 else None
    return valor

df['Estréia'] = df['Estréia'].apply(converte_lista)
df['Final'] = df['Final'].apply(converte_lista)
df['Final']

# pip install sqlalchemy == 2.0.19
# pip install --upgrade pandas sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('sqlite:///bancoSeries.db', echo=True)
df.to_sql('series.db', con=engine, if_exists='replace', index=False)
