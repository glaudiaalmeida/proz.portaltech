def calculadora():
 
    try:
      num1 = int(input("insira o primeiro número inteiro: "))
      num2 = int(input("insira o segundo número inteiro: "))
      operador = int(input
      ("Digite o número referente a operação que deseja realizar: (1. Soma; 2. Subtração; 3. Multiplicação; 4. Divisão) "))
      if (operador == 1):
        resultado = num1 + num2
        print(num1, " + ", num2, " = ", resultado)
      elif(operador == 2):
        resultado = num1 - num2
        print( num1, " - ", num2, " = ", resultado)
      elif(operador == 3):
        resultado = num1 * num2
        print( num1, " * ", num2, " = ", resultado)
        
      elif(operador == 4):
        resultado = num1 / num2
        print(num1, " / ", num2, " = ", resultado)
       else: 
        print("A calculadora foi encerrada por erros nas informações digitadas.")
    except:
      print("Por favor digite um número válido!")

calculadora()
