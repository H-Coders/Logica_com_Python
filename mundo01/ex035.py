print('-=-'*15)
print('Analisador de Triângulos')
print('-=-'*15)

v1 = float(input('Primeiro segmento: '))
v2 = float(input('Segundo segmento: '))
v3 = float(input('Terceiro segmento: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')