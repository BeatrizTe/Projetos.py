n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
print('A soma dos dois valores é {}, a subtração é {}, a multiplicação é {},'.format(a, s, m), end=' ')
print('a divisão é {:.2f} e a potência é {}'.format(d, p))
