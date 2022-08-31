# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: '))
nome2 = nome.split()
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minusculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo '.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras '.format(len(nome2[0])))












