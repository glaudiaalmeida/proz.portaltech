def nomeIdade():
    try:
      print("---------------------------")
      nome = input("insira seu nome: ")
      while (nome == ""):
        nome = input("insira seu nome: ")
      anoNasc = int(input("Insira o ano em que você nasceu: "))
      while (anoNasc < 1922) or (anoNasc > 2022):
          print("Digite um ano entre 1922 e 2022! ")
          anoNasc = int(input("Insira o ano em que você nasceu: "))
      idade = 2022 - anoNasc
    except:
       print("Você precisa digitar os dados corretamente!")
 
    print ("-----------------------------")
    print ("Seu nome é: ", nome)
    print ("Sua idade é: ", idade)

nomeIdade()

