from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
robo = randint(0, 2)

print('Suas Opções:')
print('[ 0 ] - PEDRA')
print('[ 1 ] - PAPEL')
print('[ 2 ] - TESOURA')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('-='*15)
print('O Computador jogou {}'.format(itens[robo].upper()))
print('O Jogador jogou {}'.format(itens[jogador].upper()))
print('-='*15)


if robo == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida!')

elif robo == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida!')

elif robo == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')
