# De início podem importar essas BB 
# e explico ao decorrer do código
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd

# Por conta da BB pandas ultilizamos 
# read_csv (lembrando que eu salvei minha
# planilha como csv), para passar a planilha como
# paramentros e seu separador e podemos visualizar]

# a tabela no terminal apertando o triangulo verde
contatos_df = pd.read_csv("ListaContatos.csv", sep=";")
print(contatos_df.head())

# Precisamos então ultilizar a BB selenium
# para fazer o código abrir o navegador e 
# na página do whatsApp 

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")


# Assim que logamos no Whats, o código precisa identificar
# o que tem de diferente entre a página de login
# e a página ja logado, e o que tem de diferente
# é o lado das conversas que no HTML é chamado de "side",
# então até ela aparecer vamos pedir para 
# que o código espere, por isso a BB time
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(2)
    
# Logado, precisamos então perpasar a planilha
# para o whatsapp ir na tabela numero e
# pegar cada numero especifico e enviar a 
# mensagem especifica que tem para aquele numero



for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    # Toda URL de página é meio estranha, pois elas são codificadas
    # para o browser entender o que esta ali
    # então precisamos codificar a nossa tambem 
    # ultilizando a BB urllib para então enviar a mensagem
    texto = urllib.parse.quote(f"{pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(2)
    # Apos cada mensagem diitada mas não enviada precisamos
    # envia-la, ultilizando o Xpath do botão de enviar
    # então com o botão direto do mouse você clica em 
    # cima do campo de texto do WPP e clica em inspencionar
    # ele vai abrir uma tela de HTML indicando em 
    # código o que seria aquele campo, e você copia 
    # o Xpath daquele campo colando no comando a seguir
    # para o nosso código ultilizando a BB Keys enviar a mensagem
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    # E mais uma vez temporizando os atos do código
    # para o Whatsapp não bloquear nosso número
    time.sleep(10)
    
    
