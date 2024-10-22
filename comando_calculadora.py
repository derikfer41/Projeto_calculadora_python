print('Digite um numero: ')
numero1 = int(input())

print('Digite uma operação: ')
operador = input()

print('Digite um numero: ')
numero2 = int(input())


if operador == '+':
  resultado = numero1 + numero2
  print('O resultado da operação é: ',resultado)
elif operador == '-':
  resultado = numero1 - numero2
  print('O resultado da operação é: ',resultado)
elif operador == '*':
  resultado = numero1 * numero2
  print('O resultado da operação é: ',resultado)
elif operador == '/':
  resultado = numero1 / numero2
  print('O resultado da operação é: ',resultado)
else:
  print('Operação não calculavel')
