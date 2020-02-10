import urllib
from bs4 import BeautifulSoup

url = "http://wdi.worldbank.org/table/WV.5"

html = urllib.urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')

tabela = soup.findAll('table', { 'class': 'indicators-table' })[1]

linhas = tabela.findAll('tr')

for linha in linhas:
    pais = linha.find('td', { 'class': 'country' }).text
    quantidade =  linha.findAll('td')[7].text
    print(pais + ' = ' + quantidade)