import os
import pathlib

os.chdir('C:\\Users\lucas\Desktop\python\python')
print('Diretorio atual {}'.format(os.getcwd()))

padrao_nome = input('Digite um nome para os Diretorios: ')


for contador, arq in enumerate(os.listdir()):

    if os.path.isfile(arq) and arq.endswith('.txt') and not arq.endswith('.py'):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print('Foram alterados {} arquivos'.format(contador))
print('Processo Finalizado')
