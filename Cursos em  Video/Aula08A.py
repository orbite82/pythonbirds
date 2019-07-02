import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, raiz))
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # ceil --> para cima
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) # floor --> para cima