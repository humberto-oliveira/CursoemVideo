#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Para o ãngulo de {}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é de {:.2f}'.format(ang, sen, cos, tan))

# Como o Guanabar fez:

# import math
# ângulo = float(input('Digite o ângulo que você deseja: '))
# seno = math.sin(math.radians(ângulo))
# print('O ãngulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
# cosseno = math.cos(math.radians(ângulo))
# print('O ãngulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
# tangente = math.tan(math.radians(ângulo))
# print('O ãngulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))