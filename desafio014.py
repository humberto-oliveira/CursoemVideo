# Escreva um programa que converta uma temperatura digitada em Cº e converta para Fº.

celsius = float(input('Digite a temperatura em graus celsius: '))
far = celsius * 1.8 + 32
print('Como a temperatura em graus celsius é {:.1f}ºC, em farenheit ela será de {:.1f}ºF'.format(celsius, far))

# Como o Guanabara fez:

# c = float(input('Informe a temperatura em ºC: '))
# f = 9 * c / 5 + 32
# print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
