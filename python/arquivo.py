import os
import pathlib

os.chdir('C:\\Users\lucas\Desktop\python\python')
print('Diretorio atual {}'.format(os.getcwd()))

nome_arquivo = input('Digite o nome do arquivo: ')

texto = ['Abóbora\n', 'Estilingue\n', 'Maracujá\n', 'Aconchegante\n', 'Escaparate\n', 'Girassol\n', 'Quintal\n', 'Escuna\n', 'Cachecol\n', 'Cipreste\n']

try:
    manipulador = open(nome_arquivo, 'w', encoding='UTF-8')
    manipulador.writelines(texto)
except IOError:
    print('Nao foi possivel localizar o arquivo')
else:
    manipulador.close()

try:
    manipulador = open(nome_arquivo, 'r', encoding='UTF-8')
    print(manipulador.read())
except IOError:
    print('Nao foi possivel localizar o arquivo')
else:
    manipulador.close()
