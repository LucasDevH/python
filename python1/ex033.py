a = int(input('Digite o 1º valor: '))
b = int(input('Digite o 2º valor: '))
c = int(input('Digite o 3º valor: '))
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O numero {} foi o maior digitado'.format(maior))
print('O numero {} foi o menor digitado'.format(menor))