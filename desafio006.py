# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
dob = int(n*2)
tri = int(n*3)
rai = float(n**(1/2))
print('Considerando que o número escolhido foi {}, o seu dobro é {}, seu triplo é {} e a sua raiz quadrada é {:.2f} '.format(n, dob, tri, rai))

# Como o Guanabara fez:
# Forma 1:
#
# n = int(input('Digite um número: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('O dobro de {} vale {}.'.format(n, d))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
#
# Forma 2:
#
# n = int(input('Digite um número: '))
# print('O dobro de {} vale {}.'.format(n, (n*2)))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))

