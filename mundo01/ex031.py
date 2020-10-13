distancia = float(input('Qual a distancia da sua viagem? '))

if distancia > 200:
    v1 = distancia * .45
    print('Sua viagem de {:.0f}km, vai custar: R${:.2f}.'.format(distancia, v1))
else:
    v1 = distancia * .50
    print('Sua viagem de {:.0f}km, vai custar: R$ {:.2f}.'.format(distancia, v1))
