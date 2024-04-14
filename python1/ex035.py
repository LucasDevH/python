from time import sleep
print('-='*20)
print('ANALISANDO TRIANGULOS')
print('-='*20)
sleep(1)
print('| |'*1)
sleep(1)
print('| |'*5)
sleep(1)
print('| |'*10)
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os argumentos PODEM formar um TRIANGULO')
else:
    print('Os argumentos NÃO pode formar um TRIANGULO')