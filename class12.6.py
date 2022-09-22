from datetime import date

hoje = date.today().year
nasceu = int(input('Digite o ano em que você nasceu: '))
idade = hoje - nasceu

print('Você tem {} anos.'.format(idade))

if idade <= 9:
   print('Portanto, a sua categoria é MIRIM.')
elif idade <= 14:
    print('Portanto, a sua categoria é INFANTIL.')
elif idade <= 19:
    print('Portanto, a sua categoria é JUNIOR.')
elif idade <= 25:
    print('Portanto, a sua categoria é SÊNIOR.')
else:
    print('Portanto, a sua categoria é MASTER.')