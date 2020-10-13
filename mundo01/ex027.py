nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print('Prazer em te conhecer')

print('Seu Primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))