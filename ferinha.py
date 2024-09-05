import os
# Função para limpar
def limpar():
    os.system("cls")

limpar()
produtos = ["morango","maracujá","Limão","Lima","Abacate","uva","carambola","melancia","abacaxi"] # Lista de nomes dos produtos
compra = [] # Lista de compras
precos = [7.0,13.0,2.0,5.0,4.0,10.0,90.0,2.0,10.0] # Lista de preços
desc = 0.05 # Porcentagem 0.01 = 1%
soma = 0 # A soma da compra final

escolha = int(input("Você que desconto?\n1.Sim\n2.Não\nR:")) # Requere ao usuário se vai ter dseconto ou não
limpar()
if escolha == 1: # verifica a escolha do usuário
    for i in range(len(produtos)):
        precos[i] *= (100 - desc)/100

for i in range(len(produtos)): # Imprimi a tabela da feira
    print(i+1,"º produto",produtos[i]," custa R$ ",round(precos[i],2))

# Requere ao usuário quais produtos vai comprar
compra = list(map(int,input("Quais produtos você gostaria de comprar? Escreva o número referente ao produto separado por espaço.\n").split(" ")))
# Adiciona os produtos na lista de compras
for i  in range(len(compra)):
    compra[i] = produtos[compra[i]-1]
limpar() 
print("Seu Carrinho:\n")
# Lista os produtos comprados
for i in range(len(compra)):
    print(produtos.index(compra[i])+1,"º produto",compra[i]," custa R$ ",round(precos[produtos.index(compra[i])],2))
# Soma os valores dos produtos comprados
for i in range(len(compra)):
    soma+= round(precos[produtos.index(compra[i])])
    #Exibe o total
print("\n Seu total é: ",soma)
