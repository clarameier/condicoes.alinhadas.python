from math import radians
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('Digite a sua opção de jogo.')
print('0. Pedra;')
print('1. Papel;')
print('2. Tesoura;')

jogo = int(input('Qual a sua escolha para esta jogada? '))
print('O computador jogou {}.'.format(itens[pc]))
print('Você jogou {}.'.format(itens[jogo]))

if pc == 0: #pedra
    if jogo == 0:
        print('EMPATE')
    elif jogo == 1:
        print('VOCÊ VENCEU')
    elif jogo == 2:
        print('COMPUTADOR VENCEU')
    else:
         print('Jogada inválida.')
elif pc == 1: #papel
    if jogo == 0:
        print('COMPUTADOR VENCEU')
    elif jogo == 1:
        print('EMPATE')
    elif jogo == 2:
        print('VOCÊ VENCEU')
    else:
         print('Jogada inválida.')
elif pc == 2: #tesoura
    if jogo == 0:
        print('VOCÊ VENCEU')
    elif jogo == 1:
        print('COMPUTADOR VENCEU')
    elif jogo == 2:
        print('EMPATE')
    else:
         print('Jogada inválida.')
else:
    print('Jogada inválida.')