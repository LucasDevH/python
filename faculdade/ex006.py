class Data:
    def __init__(self, d=0, m=0 , a=0):
        self.dia = d
        self.mes= m
        self.ano= a

    def input(self):
        self.dia = int(input('Entre com o dia: '))
        self.mes = int(input('Entre com o mes: '))
        self.ano = int(input('Entre com o ano: '))

    def __str__(self):
        return f'{self.dia:02}/{self.mes:02}/{self.ano:04}'

class Pessoa:
    def __init__(self, c=0, n='', d=Data()):
        self.codigo = c
        self.nome = n
        self.dtNasc= d

    def input(self):
        print('Pessoa')
        self.nome = input('Entre com o nome: ')
        self.codigo = int(input('Entre com o codigo: '))
        print('Data Nascimento')
        self.dtNasc.input()

    def __str__(self):
        aux = 'PESSOA\n=========\n'
        aux += f'Nome.............: {self.nome}\n'
        aux += f'Data nascimento ...: {self.dtNasc}'
        return aux 
    
d1 = Data()
d1.input()
print(d1)

d2 = Data(12,4,)