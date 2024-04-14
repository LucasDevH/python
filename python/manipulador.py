import os
import pathlib

os.chdir('C:\\Users\lucas\Desktop\python\python')
print('Diretorio atual {}'.format(os.getcwd()))

manipulador = open('dados0.txt', 'r', encoding='UTF-8')

# print(f'\Metodo read():\n')
# print(manipulador.read())

# print(f'\Metodo readline():\n')
# print(manipulador.readlines())

nome_arquivo = input('Digite o nome do arquivo: ')
# texto = input('Deseja procurar algum argumento? Digite o argumento ou digite NN para cancelar: ')

# try:
#     manipulador = open(nome_arquivo, 'r', encoding='UTF-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print('String encontrada')
#             print(linha)
# except IOError:
#     print('Nao foi possivel abrir o arquivo')
# else:
#     manipulador.close()
texto = input('Digite o texto: ')

try:
    manipulador = open(nome_arquivo, 'a', encoding='UTF-8')
    manipulador.write(f'\n{texto}')
    manipulador.write('\nAtt. Lucas Henrique')
except IOError:
    print('Nao foi possivel localizar o arquivo')
else:
    manipulador.close()
