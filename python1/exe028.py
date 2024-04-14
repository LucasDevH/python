from random import randint
from time import sleep
computador = randint(0, 5)
print('Pensei no numero {}'.format(computador))
jogador = int(input('Adivinhe no numero em que pensei em 0 e 5: '))
print('PROCESSANDO')
sleep(3)
if jogador == computador:
    print('Voce acertou')
else:
    print('Voce Perdeu. o numero escolhido éra {}'.format(computador))