# 2.Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.

firstNum = int(input("Digite o primeiro número: "))
secondNum = int(input("Digite o segundo número: "))
thirdNum = int(input("Digite o terceiro número: "))

if firstNum > secondNum and firstNum > thirdNum:
  print(firstNum)
elif secondNum > firstNum and secondNum > thirdNum:
  print(secondNum)
else:
  print(thirdNum)