numero = int(input('Digite um numero inteiro: '))
print('[ 1 ] Converter para BINARIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
opcao = int(input('Digite uma opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else: 
    print('Opção Desconhecida')