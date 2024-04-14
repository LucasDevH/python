class Fração:
    def __init__(self, num=1, den=1):
        self.num = num
        self.den = den

    def mostra (self):
        print(f'{self.num}/{self.den}')
        
    def toReal(self) -> float:
        return self.num / self.den

    def soma(self, f1, f2):
        a = f1.num
        b = f1.den
        c = f2.num
        d = f2.den
        if b == d:
            self.num = a + c
            self.den = b
        else:
            self.num = a*d + b*c
            self.den = b*d

# main
f1 = Fração(5, 3)
f1.mostra()
f2 = Fração(2)
f2.mostra()
f3 = Fração()
f3.mostra()

print(f1.toReal())
print(f2.toReal())
print(f3.toReal())
print('somas')
f4 = Fração(8, 3)
f5 = Fração(3, 5)
f3.soma(f1, f4)
f3.mostra()
f3.soma(f1, f5)
f3.mostra()