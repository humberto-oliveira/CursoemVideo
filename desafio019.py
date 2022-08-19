# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
al1 = str(input('Digite o nome do 1º aluno: '))
al2 = str(input('Digite o nome do 2º aluno: '))
al3 = str(input('Digite o nome do 3º aluno: '))
al4 = str(input('Digite o nome do 4º aluno: '))
print('O aluno escolhido para apagar o quadro é o {} !'.format(random.choice([al1, al2, al3, al4])))

# Como o Guanabara fez:

# import random
# n1 = str(input('Primeiro aluno: '))
# n2 = str(input('Primeiro aluno: '))
# n3 = str(input('Primeiro aluno: '))
# n4 = str(input('Primeiro aluno: '))
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print('O aluno escolhido foi {}!'.format(escolhido))







