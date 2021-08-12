l = float(input('Insira a largura da parede (em metros): '))
a = float(input('Insira a altura da parede (em metros): '))
r = l * a
t = (r / 2)
print('A parede possui {}m², para pintá-la, você precisará de {} litros de tinta.'.format(r, t))
