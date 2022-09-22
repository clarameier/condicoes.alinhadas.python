print('Qual é o seu nome?')
nome = str(input('Meu nome é '))
if nome == 'Maria':
    print('Legal, esse também é o meu nome!')
elif nome == 'Karen' or 'Karen Beatriz':
    print('Legal, esse é o nome da minha namorada!')
elif nome == 'Beatriz':
    print('Uau! Que coincidência, este nome é o mesmo de duas ex-namoradas minhas, e o segundo nome da minha namorada, que se chama Karen Beatriz!')
else:
    print('Seu nome é muito legal! Prazer te conhecer, {}!'.format(nome))