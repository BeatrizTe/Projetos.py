import math
a = float(input('Insira o valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print("O valor do seno é {:.2f}, o do cosseno é {:.2f} e da tangente é {:.2f}.".format(sen, cos, tan))
