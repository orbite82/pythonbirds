n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#print('A soma vale {}'.format(s))
print('A soma é {}, \n o produto e {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
# \n e end=' ' foi inserido para quebrar e ajuntar linha