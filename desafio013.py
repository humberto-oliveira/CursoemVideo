# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

n = float(input('Digite o seu salário: '))
novsal = 15*n/100+n
print('Como o seu salário atual é {:.2f}, com o aumento de 15% o seu novo salário será {:.2f} '.format(n, novsal))

# Como o Guanabara fez:

# salário = float(input('Qual é o salário do Funcionário: R$'))
# novo = salário + (salário * 15 / 100)
# print('Um funcionário ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))


