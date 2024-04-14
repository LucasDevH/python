salario = float(input('Digite seu salario: '))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
acrescimo = novosalario - salario
print('O seu novo salario é {} e teve um acrescimo de R${}'.format(novosalario, acrescimo))