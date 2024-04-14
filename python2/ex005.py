not1 = float(input('Digite sua 1º nota: '))
not2 = float(input('Digite sua 2º nota: '))
media = (not1 + not2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(not1, not2, media))
if media < 6 and media > 5:
    print('Você está de RECUPERAÇÂO')
elif media < 5: 
    print('Você está REPROVADO')
else:
    print('Você esta APROVADO')