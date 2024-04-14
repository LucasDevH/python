class Estoque:
    def __init__(self, nome_filial):
        self.nome_filial = nome_filial
        self._valor = 0

    def comprar(self, quantidade):
        if quantidade > 0:
            self._valor += quantidade

    def vender(self, quantidade):
        if quantidade > 0 and self._valor >= quantidade:
            self._valor -= quantidade
        else:
            print("Quantidade insuficiente em estoque.")

    @property
    def valor(self):
        return self._valor


class Produto:
    def __init__(self, nome_filial):
        self.estoque = Estoque(nome_filial)

    def comprar(self, quantidade):
        self.estoque.comprar(quantidade)

    def vender(self, quantidade):
        self.estoque.vender(quantidade)

    @property
    def nome_filial(self):
        return self.estoque.nome_filial

    @property
    def valor(self):
        return self.estoque.valor


# Exemplo de Uso
if __name__ == "__main__":
    produto = Produto("HOPPEHOSTING")
    print("Nome da Filial:", produto.nome_filial)
    print("Valor Inicial:", produto.valor)

    produto.comprar(5)
    print("Após comprar 10 unidades:", produto.valor)

    produto.vender(5)
    print("Após vender 5 unidades:", produto.valor)

    produto.vender(10)  # Isso deve gerar uma mensagem de erro, pois não há estoque suficiente
