velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    multa = 7 * (velocidade - 80) 
    print ('Voce foi multado por dirigir acima de 80Km/h')
    print ('Voce foi multado em R${:.2f} por dirigir a {}Km/h'.format(multa, velocidade))
else:
    print ('Tenha um bom dia, Dirija com segurança.')