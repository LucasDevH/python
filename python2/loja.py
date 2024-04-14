print('{:=^40}'.format(' LOJAS HOPPEHOSTING '))
valor = float(input('Digite o valor a ser pago: R$'))
print('''
[1] Dinheiro / cheque
[2] A vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao 
''')

opcao = int(input('Digite uma opção de pagamento: '))

if opcao == 1:
    total = valor - (valor * 10 / 100)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, total))
elif opcao == 3:
    total = valor
    parcela = valor / 2 
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, total))
    print('Serão 2 parcelas de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totaparcela = int(input('Quantas parcelas serão: '))
    parcela = total / totaparcela
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, total))
    print('Serão {} parcelas de R${:.2f}'.format(totaparcela, parcela))
else:
    print('Opção Invalida')
