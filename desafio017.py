#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
cop = float(input('Digite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cop, cad)
print('O comprimento da hipotenusa é {}'.format(hip))

# Como o Guanabara fez:

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))
#
# import math
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = math.hypot(co, ca)
# print('A hipotenusa vai medir {:.2f}'.format(hi))
