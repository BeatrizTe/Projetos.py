km = float(input('Insira a quantidade de kms percorridos: '))
dias = int(input('Insira a quantidade de dias pelos quais ele foi alugado: '))
total = (km * 0.15) + (dias * 60)
print('O total a pagar é de: R$ {} reais'.format(total))