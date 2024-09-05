nomes = []
numeros = []

for i in range(5):
    nome = str(input("Digite o {}º nome: ".format(i+1)))
    nomes.append(nome)

for i in range(5):
    numero = int(input("Digite o {}º número: ".format(i+1)))
    numeros.append(numero)

print("\nOs nomes digitados foram:")
for i in nomes:
    print(i)

print("\nOs números digitados foram: ")
for i in numeros:
    print(i)