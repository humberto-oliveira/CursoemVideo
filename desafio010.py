# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$3,27

dinh = float(input('Quanto dinheiro você tem na carteira? '))
n = float(dinh*(1.00/3.27))
print('Como você tem {:.2f} R$, poderá comprar {:.2f} US$ '.format(dinh, n))

# Como o Guanabara fez:

#
