#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
al1 = str(input('Qual o nome do 1º aluno? '))
al2 = str(input('Qual o nome do 2º aluno? '))
al3 = str(input('Qual o nome do 3º aluno? '))
al4 = str(input('Qual o nome do 4º aluno? '))
print('A ordem de apresentação é {}'.format(random.sample([al1, al2, al3, al4],k=4)))

# Como o Guanabara fez:

from random import shuffle

# n1 = str(input('Primeiro aluno: '))
# n2 = str(input('Segundo aluno: '))
# n3 = str(input('Terceiro aluno: '))
# n4 = str(input('Quarto aluno: '))
# lista = [n1, n2, n3, n4]
# random.shuffle(lista)
# print('A ordem de apresentação será ')
# print(lista)









