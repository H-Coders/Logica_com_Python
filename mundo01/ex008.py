metro = float(input('Uma distância em metros: '))
km = metro * .001
hm = metro * .01
dam = metro * .1
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('A medida de {}m corresponde a'.format(metro))
print('{}km'.format(km))
print('{}gm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}mm'.format(cm))
print('{:.0f}mm'.format(mm))