from datetime import date

ano_sistema = date.today().year
ano_atleta = int(input('Digite o ano do seu nascimento: '))

idade = ano_sistema - ano_atleta

print('Você tem {}anos, sua categoria é:'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIORS')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')