#R$10 X 5%
#x X 100%
#calculo de porcentagem em X
preco = float(input('Qual é o preço do produto X? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preco, novo))
