larg = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = larg * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}LT de tinta.'.format(tinta))
