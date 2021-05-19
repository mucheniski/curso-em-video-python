# Exercício Python 114:
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'Não está acessível')
else:
    print(f'Acessou')
    print(site.read()) # Mostra o conteúdo html dentro do site
