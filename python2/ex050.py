cont = 0
soma = 0

for c in range(1, 7):
    numero = int(input('Digite o {} valor: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print('Voce digitou {} valores e o resultado foi {}'.format(cont, soma))