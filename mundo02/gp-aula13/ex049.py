num = int(input('Digite o número para a tabuada? '))
print('-'*12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-'*12)