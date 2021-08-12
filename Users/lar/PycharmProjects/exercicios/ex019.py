import random
nome1 = input('Digite o nome: ')
nome2 = input('Digite o nome: ')
nome3 = input('Digite o nome: ')
nome4 = input('Digite o nome: ')
ran = [nome1, nome2, nome3, nome4]
esc = random.choice(ran)
print('O escolhido foi {}'.format(esc))
