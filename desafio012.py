#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n = float(input('Digite o preço do produto: '))
desc = float(n-(n*5/100))
print ('O produto que tinha o valor {:.2f}, agora com desconto de 5% terá o valor de {:.2f}'.format(n, desc))

# Como o Guanabara fez:

# preço = float(input('Qual é o preço do produto? R$'))
# novo = preço - (preço * 5/100)
# print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
