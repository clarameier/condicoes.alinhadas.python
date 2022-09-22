p1 = float(input('Digite sua primeira nota: '))
p2 = float(input('Digite sua segunda nota: '))
media = (p1 + p2) / 2
print('Sua média foi de: {:.1f}.'.format(media))

if media < 5.0:
    print('REPROVADO!')
elif 7 > media <= 5.0:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO!')