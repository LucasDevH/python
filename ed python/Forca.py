import random

class Forca:
    def __init__(self, palavra, dica):
        # Inicializa os atributos da instância
        self.palavra = palavra.upper()  # Converte a palavra para maiúsculas
        self.dica = dica
        self.palavra_oculta = '_' * len(palavra)  # Cria uma string com sublinhados para representar letras não reveladas
        self.letras_erradas = []  # Lista para armazenar letras erradas
        self.max_tentativas = 6  # Número máximo de tentativas permitidas
        self.tentativas = 0  # Contador de tentativas

    def mostrar_palavra(self):
        # Retorna a palavra a ser adivinhada, com letras reveladas e não reveladas
        return ' '.join(self.palavra_oculta)

    def tentar_letra(self, letra):
        letra = letra.upper()  # Converte a letra inserida para maiúsculas
        if letra in self.palavra:
            # Se a letra está na palavra, substitui os sublinhados pelas letras correspondentes
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.palavra_oculta = self.palavra_oculta[:i] + letra + self.palavra_oculta[i+1:]
            if '_' not in self.palavra_oculta:
                return True  # Retorna True se a palavra foi completamente adivinhada
        else:
            # Se a letra não está na palavra, adiciona à lista de letras erradas e incrementa o contador de tentativas
            self.letras_erradas.append(letra)
            self.tentativas += 1
            if self.tentativas >= self.max_tentativas:
                return False  # Retorna False se o jogador excedeu o número máximo de tentativas
        return None  # Retorna None se o jogo ainda está em andamento

    def obter_palavra(self):
        # Retorna a palavra a ser adivinhada
        return self.palavra

    def obter_dica(self):
        # Retorna a dica associada à palavra
        return self.dica

    def obter_letras_erradas(self):
        # Retorna as letras erradas que o jogador tentou
        return ', '.join(self.letras_erradas)

    def obter_tentativas_restantes(self):
        # Retorna o número de tentativas restantes antes de o jogador perder o jogo
        return self.max_tentativas - self.tentativas

    def verificar_status(self):
        # Verifica o status atual do jogo
        if '_' not in self.palavra_oculta:
            return 'venceu'  # Retorna 'venceu' se o jogador adivinhou todas as letras da palavra
        elif self.tentativas >= self.max_tentativas:
            return 'perdeu'  # Retorna 'perdeu' se o jogador excedeu o número máximo de tentativas
        else:
            return 'em andamento'  # Retorna 'em andamento' se o jogo ainda está em andamento
        
    def desenhar_forca(self):
        # Desenha a representação visual da forca, mostrando o progresso do jogo
        print("Forca:")
        print("  ____")
        print(" |    |")
        print(" |    " + ("O" if len(self.letras_erradas) > 0 else ""))
        print(" |   " + ("/" if len(self.letras_erradas) > 2 else "") + ("|" if len(self.letras_erradas) > 1 else "") +
              ("\\" if len(self.letras_erradas) > 3 else ""))
        print(" |   " + ("/" if len(self.letras_erradas) > 4 else "") + " " + ("\\" if len(self.letras_erradas) > 5 else ""))
        print("_|_")


class GeradorPalavras:
    def __init__(self):
        # Inicializa uma lista de palavras e suas respectivas dicas
        self.palavras = [
            ('PYTHON', 'Uma linguagem de programação'),
            ('FORCA', 'Um jogo clássico de palavras'),
            ('BISCOITO', 'Uma comida deliciosa'),
            ('ELEFANTE', 'Um animal grande e forte'),
            ('ABACAXI', 'Uma fruta tropical'),
            ('CADEIRA', 'Um móvel para sentar'),
            ('INTERNET', 'Uma rede global de computadores'),
            ('PRAIA', 'Um lugar para relaxar na areia'),
            ('ARVORE', 'Uma planta alta com galhos'),
            ('COMPUTADOR', 'Uma máquina para processamento de dados')
        ]

    def gerar_palavra(self):
        # Retorna uma palavra aleatória da lista de palavras
        return random.choice(self.palavras)
