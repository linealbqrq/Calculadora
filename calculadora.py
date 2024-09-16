#Calculadora

nome = input('Digite seu nome')

print('Olá,',nome, '. Vamos calcular?')
print('Digite dois números')

num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')


num1_convert = float(num1)
num2_convert = float(num2)

if num1.isnumeric() == False or num2.isnumeric() == False:
  print('Número inválido')
  num1 = input('Digite o primeiro número: ')
  num2 = input('Digite o segundo número: ')
  num1_convert = float(num1)
  num2_convert = float(num2)


else:
  print('Lista de Operações')

#lista de operações

lista = {'Soma', ' Subtração', ' Multiplicação', ' Divisão'}

'''for i, val in enumerate(lista):
  print(i, val)'''

print('Digite 0 para somar')
print('Digite 1 para subtrair')
print('Digite 2 para multiplicar')
print('Digite 3 para dividir')

print('Qual operação deseja fazer?')


# resultados
while True:
  opcao = int(input('Digite o número da operação que deseja realizar: '))
  opcao_convert = int(opcao)

  if opcao == 0:
    sum = num1_convert + num2_convert
    print('Você escolheu Somar')
    print('O resultado da soma de', num1, '+', num2, 'é', sum)

  elif opcao == 1:
    sub = num1_convert - num2_convert
    print('Você escolheu Subtrair')
    print('O resultado da soma de', num1, '-', num2, 'é', sub)


  elif opcao == 2:
    mult = num1_convert * num2_convert
    print('Você escolheu Multiplicar')
    print('O resultado da soma de', num1, '*', num2, 'é', mult)


  elif opcao == 3:
    div = num1_convert / num2_convert
    print('Você escolheu Dividir')
    print('O resultado da soma de', num1, '/', num2, 'é', div)

  opcao = input('Deseja realizar outra operação? Digite sim ou não: ')
  if opcao == 'sim':
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    num1_convert = float(num1)
    num2_convert = float(num2)
    continue
  else:
    print('Ok :)')
    break

