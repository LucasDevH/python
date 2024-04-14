numero = int(input('Digite um numero para ver sua tabuada: '))
multiplicador = 1

for tabuada in range(1, 11):
    resultado = numero * multiplicador
    print('{} x {} = {}'.format(numero, multiplicador, resultado))
    multiplicador = multiplicador + 1