
sexo = str(input('Qual é o seu sexo? [F/M] ')).upper()[0].strip()

print(sexo)

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso.'.format(sexo))