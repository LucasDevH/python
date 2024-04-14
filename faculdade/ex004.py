class carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar_carro(self):
        print(f'Ligando Motor do {self.modelo}')

    def desligar_carro(self):
        print('Desligando Motor do {}'.format(self.modelo))

gol = carro('wv','gol','2014','branco')
gol.ligar_carro()
gol.desligar_carro()