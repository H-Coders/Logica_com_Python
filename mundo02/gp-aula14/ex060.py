from math import factorial

num = int(input('Digite um número para calcular seu Fatorial: '))
# fat = factorial(num)
c = num
f = 1
print('Calculando {}! = '.format(num))
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    print(f)
    c -= 1
# print('O fatorial de {} é {}.'.format(num, fat))