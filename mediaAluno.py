'''
Escreva um programa em Python que recebe como entrada uma lista de tuplas, onde
cada tupla contém o nome de um aluno e suas três notas. O programa deve calcular
a média das notas de cada aluno e exibir o nome do aluno juntamente com sua
média. Em seguida, o programa deve exibir a média geral da turma.
'''
def main():
    soma_geral = 0
    media_alunos=[]
    notas = []
    alunos = list(input("Digite a o nome do alunos e suas notas no formato: nome, nota, nota, nota, nota; nome, nota, nota, nota\n").split('; '))

    for i in range(len(alunos)):
        notas.append(tuple(alunos[i].split(', ')))
    
    for aluno in notas:
        soma = 0
        for i in aluno:
            if aluno.index(i) != 0:
                soma += float(i)
        media_alunos.append(soma/4)
    
    for tupla in notas:
            print(f"\n{tupla[0]}: "
                  f"\n1º nota: {tupla[1]}"
                  f"\n2º nota: {tupla[2]}"
                  f"\n3º nota: {tupla[3]}"
                  f"\n4º nota: {tupla[4]}"
                  f"\nMédia: {media_alunos[notas.index(tupla)]:.2f}")
    
    for media in media_alunos:
         soma_geral += media
        
    print("\nMédia geral da turma: ",round(soma_geral/len(notas),2))
            
    

if __name__ == "__main__":
    main()