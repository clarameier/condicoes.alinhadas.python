peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}!'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso normal!')
elif 25 <= imc < 30:
    print('Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em obesidade!')
elif imc >= 40:
    print('Você está em obesidade mórbida!')
