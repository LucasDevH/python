peso = float(input('Qual seu Peso em (Kg)? '))
altura = float(input('Qual sua altura? '))
imc= peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 20 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')