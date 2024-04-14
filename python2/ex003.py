nun1 = int(input('Digite um numero: '))
nun2 = int(input('Digite outro numero: '))

if nun1 == nun2:
    print('Os numeros são IGUAIS')
elif nun1 > nun2:
    print('O {} é MAIOR que o {}'.format(nun1, nun2))
else:
    print('O {} é MENOR que o {}'.format(nun1, nun2))