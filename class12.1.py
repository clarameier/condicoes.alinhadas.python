#variáveis principais
casa = float(input('Qual o valor da casa que você deseja? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você deseja pagar a casa? '))

prestacao = casa / (anos * 12)
excedente = salario * 0.30

print('Para pagar uma casa de {:.2f} reais em apenas {} anos, a prestação será de {:.2f} reais.'.format(casa, anos, prestacao))

#prestação mensal e condições
if prestacao >= excedente:
    print('Portanto, sentimos muito, o seu empréstimo foi negado!')
else:
    print('Portanto, parabéns, o seu empréstimo foi aprovado!')