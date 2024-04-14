numero = int(input('Digite um numero: '))
resultado = numero % 2
if resultado == 1:
    print('O numero {} é impar'.format(numero))
else:
    print('O numero {} é par'.format(numero))