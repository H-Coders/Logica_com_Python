
print('-=-'*15)
print('Analisador de Triângulos')
print('-=-'*15)

v1 = float(input('Primeiro segmento: '))
v2 = float(input('Segundo segmento: '))
v3 = float(input('Terceiro segmento: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if v1 == v2 == v3:
        print('EQUILATERO!')
    elif v1 != v2 != v3 != v1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')
