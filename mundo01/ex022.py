nome = input('Digite sue nome COMPLETO: ').strip()

print('Seu nome em Maiusculo é {}'.format(nome.upper()))
print('Seu nome em Minusculo é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome.strip(' ')))) # len(nome) - nome.count(' ')
# separa = nome.split()
# print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))