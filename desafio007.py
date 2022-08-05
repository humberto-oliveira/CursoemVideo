# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = float((n1+n2)/2)
print('Como as suas notas foram {} e {}, a sua média é {:.1f}! '.format(n1, n2, media))

# Como o Guanabaa fez:

# n1 = float(input('Primeira nota do aluno: '))
# n2 = float(input('Segunda nota do aluno: '))
# média = (n1 + n2) / 2
# print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
