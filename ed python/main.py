import random
# Importa a biblioteca pandas para manipulação de dados em formato tabular
import pandas as pd
# Importa a biblioteca os para manipulação de funcionalidades dependentes do sistema operacional
import os

# Importa as classes Forca e GeradorPalavras do arquivo Forca.py
from Forca import *


class JogoDaForca:
    def __init__(self):
        # Inicializa os atributos necessários para o jogo
        self.forca = None  # Instância da classe Forca
        self.gerador_palavras = GeradorPalavras()  # Instância da classe GeradorPalavras
        self.ranking = {}  # Dicionário para armazenar o ranking dos jogadores

    def iniciar_jogo(self):
        print("Bem-vindo ao Jogo da Forca!")
        jogador = input("Digite seu nome: ")
        while True:
            # Gera uma palavra e uma dica utilizando o GeradorPalavras
            palavra, dica = self.gerador_palavras.gerar_palavra()
            self.forca = Forca(palavra, dica)  # Inicializa o jogo com a palavra e a dica
            self.jogar()  # Inicia o jogo
            resultado = self.forca.verificar_status()  # Verifica o resultado do jogo
            if resultado == 'venceu':
                print("Parabéns! Você acertou a palavra!")
                # Calcula a pontuação do jogador e atualiza o ranking
                pontuacao = len(self.forca.obter_palavra()) * self.forca.obter_tentativas_restantes()
                self.atualizar_ranking(jogador, pontuacao)
            elif resultado == 'perdeu':
                print("Você perdeu! A palavra era:", self.forca.obter_palavra())
            opcao = input("Deseja jogar novamente? (S/N): ")
            if opcao.upper() != 'S':
                break
        self.mostrar_ranking()  # Exibe o ranking ao final do jogo

    def jogar(self):
        print("\nDica:", self.forca.obter_dica())
        print("Palavra:", self.forca.mostrar_palavra())
        while True:
            letra = input("Digite uma letra: ")
            resultado = self.forca.tentar_letra(letra)
            if resultado == True:
                print("Parabéns! Você acertou a letra!")
                break
            elif resultado == False:
                print("Você errou muitas vezes. A palavra era:", self.forca.obter_palavra())
                break
            else:
                print("Letra errada! Tentativas restantes:", self.forca.obter_tentativas_restantes())
                print("Letras erradas:", self.forca.obter_letras_erradas())
            self.forca.desenhar_forca()  # Desenha a forca
            print("\nDica:", self.forca.obter_dica())
            print("Palavra:", self.forca.mostrar_palavra())

    def atualizar_ranking(self, jogador, pontuacao):
        # Atualiza o ranking do jogador com sua pontuação
        if jogador in self.ranking:
            self.ranking[jogador] += pontuacao
        else:
            self.ranking[jogador] = pontuacao
        self.salvar_ranking()  # Salva o ranking atualizado

    def mostrar_ranking(self):
        print("\n=== RANKING ===")
        # Carrega o ranking a partir do arquivo CSV e exibe na tela
        ranking_ordenado = pd.read_csv('C:\\Users\\lucas\\Desktop\\python\\forca2\\ranking.csv')
        print(ranking_ordenado)

    def salvar_ranking(self):
        # Salva o ranking atualizado em um arquivo CSV
        df = pd.DataFrame(list(self.ranking.items()), columns=['Jogador', 'Pontuação'])
        df.to_csv('C:\\Users\\lucas\\Desktop\\python\\forca2\\ranking.csv', index=False, mode='a', header=not os.path.exists('C:\\Users\\lucas\\Desktop\\python\\forca2\\ranking.csv'))

if __name__ == "__main__":
    jogo = JogoDaForca()
    jogo.iniciar_jogo()
