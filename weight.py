# 3.Tendo como dados de
# entrada a altura e o sexo de uma pessoa (M masculino e F feminino), construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# para homens: (72.7*h)-58
# para mulheres: (62.1*h)-44.7

height = float(input('Digite sua altura: '))
sex = input('Digite seu sexo (M/F): ')

if sex == 'M' or sex == 'm':
  idealWeight = (72.7 * height) - 58
  print(f'Seu peso ideal é {"{:.2f}".format(idealWeight)}kg')
elif sex == 'F' or sex == 'f':
  idealWeight = (62.1 * height) - 44.7
  print(f'Seu peso ideal é {"{:.2f}".format(idealWeight)}kg')
else:
  print('Por favor, digite F ou M para seu sexo')