import math
x = float(input('Insira o valor do cateto oposto: '))
y = float(input('Insira o valor do cateto adjacente: '))
h = math.hypot(x, y)
print('O valor da hipotenusa é {:.2f}.'.format(h))
