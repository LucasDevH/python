class Somador:
    def __init__(self, v=0):
        self.valor = v

    def soma(self, v):
        self.valor += v

    def getValor(self):
        return self.valor
    
    def __str__(self):
        print(f'Somador={self.valor}')


class Media:
    def __init__(self):
        self.soma = Somador()
        self.qtd = Somador()

    def adicionar(self, v):
        self.soma.soma(v)
        self.qtd.soma(1)
    
    def getMedia(self):
        return self.soma.getValor() / self.qtd.getValor()
    
    def __str__(self):
        aux = f'Total: {self.soma.getValor()}'
        aux += f'\nQuantidade: {self.qtd.getValor()}'
        aux += f'\nMedia: {self.getMedia()}'
        return aux 
    
# main

m1 = Media()
valor = 0

while valor >= 0:
    valor = float(input('Digite um valor positivo (negativo encerra): '))
    if valor > 0:
        m1.adicionar(valor)

    print( m1 )