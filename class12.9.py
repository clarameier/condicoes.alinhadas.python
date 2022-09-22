#variáveis
prod = float(input('Digite o valor total da sua compra: R$'))
vista = prod * 0.10
card = prod * 0.05
x2 = prod / 2
x3 = prod * 0.20

#opções pagamento
print('Digite a opção que deseja pagar.')
print('1. À vista (dinheiro/cheque);')
print('2. À vista (cartão);')
print('3. 2x no cartão.')
print('4. 3x no cartão.')
opcao = int(input('A opção escolhida foi: '))

#condições
if opcao == 1:
    print('Se você pagar a vista, em dinheiro ou cheque, receberá um desconto de {:.2f} reais.'.format(vista))
elif opcao == 2:
    print('Se você pagar à vista, no cartão, receberá um desconto de {:.2f} reais.'.format(card))
elif opcao == 3:
    print('Se você pagar em até 2x no cartão, o valor do produto será o mesmo, pagando {:.2f} reais por mês.'.format(x2))
elif opcao == 4:
    print('Se você pagar no cartão, parcelando em 3x ou mais no cartão, então o seu produto terá juros de 20%, totalizando {:.2f} reais.'.format(x3))
else:
    print('Opção inválida, por favor, tente novamente digitando apenas 1, 2, 3 ou 4.')