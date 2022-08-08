# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número:6.127. O número 6.127 tem a parte inteira 6.

from math import trunc
n = float(input('Digite um número real: '))
print('Como o número digitado foi {}, sua porção inteira é {}'.format(n, trunc(n)))
#
# Como o Guanabara fez:

# import math
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

# from math import trunc
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
