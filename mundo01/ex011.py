lp = float(input('Largura da Parede: '))
ap = float(input('Altura da Parede: '))
area = lp*ap

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lp, ap, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/2))