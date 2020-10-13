from random import randint
from time import sleep

print('=--'*15)
print('ESTOU PENSANDO EM UM NUMERO, ENTRE 0 A 5')
print('=--'*15)
sleep(1)
num = int(input('Em que numero eu pensei? '))
numrandom = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
#Condição
if num == numrandom:
    print('Você venceu')
else:
    print('Você perdeu, eu pensei no número {}. Tente novamente.'.format(numrandom))