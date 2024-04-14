from tkinter import *
from requests import *
from random import randint

palavras = ('cachorro', 'bola', 'casa', 'livro', 'sol', 'agua', 'gato', 'comida', 'amigo', 'feliz')

forca = randint(0 , 9)
chance = 7

#teste

palavra_escolida = (palavras[forca])
letras_usuario = []

if forca == 0:
    dica = ('Animal de estimação conhecido por sua lealdade aos humanos.')
elif forca == 1:
    dica = ('Objeto redondo frequentemente usado em jogos como futebol ou basquete.')
elif forca == 2:
    dica = ('Lugar onde as pessoas vivem e se abrigam.')
elif forca == 3:
    dica = ('Conjunto de páginas com informações ou histórias impressas.')
elif forca == 4:
    dica = ('Estrela ao redor da qual a Terra orbita, fornecendo luz e calor.')
elif forca == 5:
    dica = ('Substância transparente e incolor essencial para a vida.')
elif forca == 6:
    dica = ('Animal de estimação conhecido por sua independência e agilidade.')
elif forca == 7:
    dica = ('Alimento necessário para sustentar a vida.')
elif forca == 8:
    dica = ('Pessoa com quem se tem um vínculo próximo e de confiança.')
elif forca == 9:
    dica = ('Estado emocional caracterizado por contentamento e alegria.')
else:
    dica = ('SEM DICA')

print(dica)

while True:

    for letra in palavra_escolida:

        if letra.lower() in letras_usuario:

            print(letra, end=" ")

        else:

            print("_", end=" ")

    print(f"Você tem {chance} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")

    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra_escolida.lower():

        chance -= 1

    ganhou = True

    for letra in palavra_escolida:

        if letra.lower() not in letras_usuario:

            ganhou = False

    if chance == 0 or ganhou:
        break

    if chance == 7:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif chance == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif chance == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |     __|    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif chance == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |     __|__   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    elif chance == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |     __|__   ")
        print(" |       |    ")
        print(" |       |     ")
        print(" |            ")
        print("_|___         ")
        print()
    elif chance == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |     __|__   ")
        print(" |       |    ")
        print(" |      _|    ")
        print(" |            ")
        print("_|___         ")
        print()
    elif chance == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |     __|__   ")
        print(" |       |    ")
        print(" |      _|_  ")
        print(" |            ")
        print("_|___         ")
        print()

if ganhou:

    print(f"Parabéns, você ganhou. A palavra era: {palavra_escolida}")

else:

    print(f"Você perdeu! A palavra era: {palavra_escolida}")


    

#janela = Tk()
#janela.title('JOGO DA FORCA')

#janela.mainloop()

