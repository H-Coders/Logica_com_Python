from time import sleep 

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0

while menu != 5:
    print('''
    ### MENU ###
    [ 1 ] - SOMA
    [ 2 ] - MULTIPLICAR
    [ 3 ] - MAIOR
    [ 4 ] - NOVOS NUMEROS
    [ 5 ] - SAIR
    ----------------------''')
    menu = int(input('>>> Escolha a opção desejada: '))

    if menu == 1:
        num = n1 + n2
        print(num)
        sleep(2)
    elif menu == 2:
        num = n1 * n2
        print(num)
        sleep(1)
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('{} é o maior número.'.format(maior)) 
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Obrigado por usar nossos sistemas!')
        sleep(1)
        print('Finalizando...')
        sleep(1)
    else:
        print('Numero inválido!')
        print('Escolha um número entre 1 - 5!')
    print('-=' * 15)
print('Fim do programa! Volte Sempre!')