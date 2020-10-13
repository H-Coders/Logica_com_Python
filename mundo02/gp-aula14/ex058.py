from random import randint
from time import sleep

print('=--'*15)
print('ESTOU PENSANDO EM UM NUMERO, ENTRE 0 A 10')
print('=--'*15)
sleep(1)
numrandom = randint(0, 10)
print('PROCESSANDO...')
sleep(3)
#Condição
acertou = False
cont = 0
while not acertou:
    num = int(input('Em que numero eu pensei? '))
    sleep(1)
    cont += 1
    if num == numrandom:
        print('PARABENS, Você venceu')
        print('Você precisou de {} palpites para vencer. (:'.format(cont))
        acertou = True
    elif num > 10:
        print('LEMBRE, é sø até 10!')
    else:
        if num < numrandom:
            print('Mais... Tente mais uma vez!')
        else:
            print('Menos... Tente mais uma vez!')
