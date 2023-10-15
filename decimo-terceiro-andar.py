
# for i in range(21):
#     if (i == 0):
#         print("Este é o térreo.")
#     elif (i != 0 and i != 13):
#         print("Este é o ", i, " andar.")

# i = 0
# while (i <= 20):
#     if (i == 0):
#         print("Este é o térreo.")
#     elif (i != 0 and i != 13):
#         print("Este é o ", i, " andar.")
#     i = i + 1

# numero = 0
# if (numero == 0):
#     print("Este é o térreo.")
#     numero += 1
# while (numero <= 20):
#     if (numero != 13):
#         print("Este é o ", numero, " andar.")
#     numero = numero + 1

# no decremento não consegui imprimir o andar térreo(código abaixo)
for i in range(20, 0, -1):
    if (i != 13):
        print("Este é o ", i, " andar.")
    else:
        print("Este é o térreo.")