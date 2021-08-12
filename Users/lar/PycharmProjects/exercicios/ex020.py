import random
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
rand = random.sample([nome1, nome2, nome3, nome4], k=4)
print('A ordem de apresentação será {}'.format(rand))