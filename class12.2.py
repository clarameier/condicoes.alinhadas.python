numero = int(input('Digite um número inteiro qualquer: '))

print('Digite a opção que deseja para a sua conversão.')
print('1. Binário;')
print('2. Octal;')
print('3. Hexadecimal.')
opcao = int(input('A opção escolhida foi: '))

if opcao == 1:
    print('O número escolhido foi {} e convertido para um número binário fica como {}.'.format(numero, bin(numero) [2:]))
elif opcao == 2:
    print('O número escolhido foi {} e convertido para um número octal fica como {}.'.format(numero, oct(numero) [2:]))
elif opcao == 3:
    print('O número escolhido foi {} e convertido para um número hexadecimal fica como {}.'.format(numero, hex(numero) [2:]))
else:
    print('Opção inválida, por favor, tente novamente digitando apenas 1, 2 ou 3.')
