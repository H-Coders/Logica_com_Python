altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite seu peso: (kg) '))

# imc = peso / (altura * altura)
imc = peso / (altura ** 2)

print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and imc < 25:
    print('Peso Ideal')
elif imc > 25 and imc < 30:
    print('Sobre Peso')
elif imc > 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')
