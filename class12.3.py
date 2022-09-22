num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O primeiro valor escolhido é maior que o segundo! Ou seja, {} > {}.'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor escolhido é maior que o primeiro! Ou seja, {} > {}.'.format(num2, num1))
else:
    print('Os dois números são iguais!')