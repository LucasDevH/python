valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos quer pagar: '))

pretacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f}'.format(valor, anos, pretacao))

if pretacao <= minimo:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')