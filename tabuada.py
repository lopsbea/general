num = int(input('Digite um número inteiro: '))

# print('1 x', n, '=', n*1)
  
for i in range(50000):
  result = num*i
  print(f'{num} x {i} = {result}')
