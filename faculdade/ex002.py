class produto1:
    def __init__(self, preço):
        self.preço = preço

#p = produto1(200)
#print('Preço = {}'.format(p.preço))
#p.preço = -50
#print('preço = {}'.format(p.preço))

class produto2:
    def __init__(self, preço):
        self.__preço = preço

    def getPreço(self):
        return self.__preço
    
    def setPreço(self, preço):
        if preço > 0:
            self.__preço = preço
        else:
            print('PREÇO INVALIDO')

p2 = produto2(200)
print('Preço = {}'.format(p2.getPreço()))
p2.setPreço(250)
print('Preço = {}'.format(p2.getPreço()))

class produto3:
    def __init__(self, preço):  
        self.__preço = preço

    @property
    def preço(self):
        return self.__preço
    
    @preço.setter
    def preço(self, preço):
        if preço > 0:
            self.__preço = preço
        else:
            print('PREÇO INVALIDO')

#p = produto3(200)
#print('Preço= {}'.format(p.preço))
#p.preço = 250
#print('Preço = {}'.format(p.preço))
