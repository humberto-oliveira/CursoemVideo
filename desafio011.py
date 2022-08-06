# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

# +

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
tinta = area / 2
print('Considerando a área de {}, a quantidade de tinta necessária é {:.1f}!'.format(area, tinta))

# Como o Guanabara fez:

# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# área = larg * alt
# print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
# tinta = área / 2
# print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

