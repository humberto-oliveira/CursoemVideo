# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
suc = int(n+1)
ant = int(n-1)
print('Considerando que o número escolhido foi {}, o seu sucessor é {} e o seu antecessor é {}. '.format(n, suc, ant))

# Como o Guanabara fez:

# Forma 1:

# n = int(input('Digite um número: '))
# a = n - 1
# s = n + 1
# print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

# Forma 2:

# n = int(input('Digite um número: '))
# print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

