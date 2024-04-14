from random import randint
from time import sleep

maquina = randint(1, 3)

print('A maquina escolheu a opção {}'.format(maquina))

print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')
jogada = int(input('Qual sua jogada? '))


if jogada == 1:
    escolha = 'PEDRA'
elif jogada == 2:
    escolha = 'PAPEL'
elif jogada == 3:
    escolha = 'TESOURA'

if maquina == 1:
    escolham = 'PEDRA'
elif maquina == 2:
    escolham = 'PAPEL'
elif maquina == 3:
    escolham = 'TESOURA' 

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ') 
sleep(1)  

if jogada == 1 and maquina == 1:
    print('EMPATE')
elif jogada == 1 and maquina == 2:
    print('MAQUINA GANHOU')
elif jogada == 1 and maquina == 3:
    print('VOCE GANHOU')
elif jogada == 2 and maquina == 1:
    print('VOCE GANHOU')
elif jogada == 2 and maquina == 2:
    print('EMPATE')
elif jogada == 2 and maquina == 3:
    print('MAQUINA GANHOU')
elif jogada == 3 and maquina == 1:
    print('MAQUINA GANHOU')
elif jogada == 3 and maquina == 2:
    print('VOCE GANHOU')
elif jogada == 3 and maquina == 3:
    print('EMPATE')
else:
    ('OPÇÂO INVALIDA')

print('-='*40)
print('Voce jogou {} e a maquina jogou {}'.format(escolha, escolham))
print('-='*40)
