dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * .15)
print('O total a pagar é de R${:2}'.format(pago))