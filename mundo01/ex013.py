salario = float(input('Qual é o seu salário? R$'))
novo = salario + (salario * 15 / 100)

print('O seu salário que era R${}, com os 15% de aumento vai ficar R${:.2f}'.format(salario, novo))