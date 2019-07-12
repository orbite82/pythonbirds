#import math
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hi = math.hypot(co, ca)
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
