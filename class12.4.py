from datetime import date
hoje = date.today().year
nasceu = int(input('Digite o ano em que você nasceu: '))
idade = hoje - nasceu

print('Segundo nossos dados, você nasceu em {}, e tem {} anos em {}.'.format(nasceu, idade, hoje))

if idade < 18:
    print('Você ainda vai se alistar ao serviço militar!')
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para isto!'.format(saldo))
elif idade == 18:
    print('Este é o ano em que você deve se alistar ao serviço militar!')
else:
    print('Agora já passou do seu tempo de alistamento ao serviço militar.')
    saldo = idade - 18
    print('O seu prazo de alistamento passou tem {} ano(s)!'.format(saldo))