# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metr = float(input('Digite um valor em metros: '))
cent = float(metr*100)
mili = float(metr*1000)
print('Como o valor em metros é {}, em centimetros será {:.0f} e em milimetros será {:.0f}! '.format(metr, cent, mili))

# Como o Guanabara fez:

# medida = float(input('Uma distancia em metros: '))
# cm = medida * 100
# mm = medida * 1000
# print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))


