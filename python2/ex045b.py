from random import randint

dados = ('PEDRA', 'PAPEL', 'TESOURA')

maquina = randint(0, 2)

print('A maquina escolheu {}'.format(dados[maquina]))