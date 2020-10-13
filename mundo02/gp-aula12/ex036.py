print('-=-'*15)
print('Emprestimo NuBank - (COMPRE SUA CASA AGORA)')
print('-=-'*15)
valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual seu salário? '))
parcelas = int(input('Num. Parcelas: '))

minimo = salario * 30/100
prestacao = valor_casa / (parcelas * 12)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, parcelas), end='')
print(' a prestação será de R${:.2f}.'.format(prestacao))


if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')