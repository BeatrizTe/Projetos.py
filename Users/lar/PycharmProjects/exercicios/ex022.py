nome = input('Digite o seu nome completo: ')
nomeu = nome.upper()
nomel = nome.lower()
nomesem = nome.split()
total = len(nomesem)
primeiron = len(nome)
print('''Nome em maiúsculo: {}
Nome em minúsculo: {}
Total de caracteres: {} 
Total de caracteres do primeiro nome: {}'''.format(nomeu, nomel, total, primeiron))