from datetime import date
ano_sistema = date.today().year

print('''
        ###### BEM VINDO AO ALISTAMENTO #####
        DIGITE O NUMERO DESEJADO PARA O ALISTAMENTO
        [ 1 ] - HOMEM
        [ 2 ] - MULHER
''')
opcao = int(input('Digite sua opção: '))
print('-='*10)
if opcao == 1:
    ano_recruta = int(input('Informe seu ano de nascimento: '))
    tempo = ano_sistema - ano_recruta
    print('ele')
elif opcao == 2:
    ano_recruta = int(input('Informe seu ano de nascimento: '))
    tempo = ano_sistema - ano_recruta
    print('ela')
else:
    print('Digite uma opção válida!')
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_recruta, tempo, ano_sistema))

if tempo == 18:
    print('Está na hora de se alistar!')
elif tempo < 18:
    saldo = 18 - tempo
    print('Ainda não esta na hora de se alistar!')
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = ano_sistema + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif tempo > 18:
    saldo = tempo - 18
    ano = ano_sistema - saldo
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Passou do tempo de se alistar! Vai pagar multa....')
    print('Seu alistamento foi em {}.'.format(ano))
print('-='*10)

