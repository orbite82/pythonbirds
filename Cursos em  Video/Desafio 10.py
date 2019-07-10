real = float(input('Quanto dinheiro você tem em sua carteira ? R$'))
dolar = real / 3.78
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))