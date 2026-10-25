print("---------------")
print('[--CALCULADORA--]')
print("---------------")

numero1 =int( input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))

print('Escolha a operação:')
print('1- Soma')
print('2- Subtração')
print('3- multplicação') 
print('4- Divisão')

operacao= input('digite o número da operação desejada:')

if operacao == "1":
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")
elif operacao == "2":
    resultado = numero1 - numero2
    print(f"Resultado da subtração: {resultado}")
elif operacao == "3":
    resultado = numero1 * numero2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == "4":
    resultado = numero1 / numero2
    print(f"Resultado da divisão: {resultado}") 
else:print("--->[OPERAÇÃO INVÁLIDA OU NÃO ATRIBUIDA]<---")