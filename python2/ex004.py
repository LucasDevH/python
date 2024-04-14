from datetime import date
anonascimento = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year

idade = anoatual - anonascimento
print('Quem nasceu em {} tem {} anos em {}'.format(anonascimento, idade, anoatual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
else:
    print('Você deveria ter se alistado a {} anos'.format(idade - 18))
