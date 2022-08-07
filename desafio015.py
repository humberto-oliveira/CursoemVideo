#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmperc = float(input('Qual a quantidade de Km percorridos com o carro alugado? '))
qtddias = int(input('Qual a quantidade de dias o carro ficou alugado? '))
preço = float(60 * qtddias + 0.15 * kmperc)
print('Como o carro andou {} Kms em {} dias, o preço a pagar é:R$ {:.2f} '.format(kmperc, qtddias, preço))

#Como o Guanabara fez:

# dias = int(input('Quantos dias alugados? '))
# km = float(input('Quantos Km rodados? '))
# pago = (dias * 60) + (km * 0.15)
# print('O total a pagar é de R${:.02f}'.format(pago))
