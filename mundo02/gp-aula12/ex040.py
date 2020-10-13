nota1 = float(input('Insira a primera nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

print('Sua média foi {}'.format(media))

if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
# elif media >= 5 and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('Parabéns, APROVADO')