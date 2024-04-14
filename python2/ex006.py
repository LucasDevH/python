from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    classificação = ('MIRIM')
elif idade > 9 and idade <= 14:
    classificação = ('INFANTIL')
elif idade > 14 and idade <= 19:
    classificação = ('JÚNIOR')
elif idade > 19 and idade <= 25:
    classificação = ('SENIOR')
else:
    classificação = ('MASTER')

print('Classificação {}'.format(classificação))
