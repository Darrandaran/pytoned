"""
Escreava um programa em Python que recebe duas tuplas de números inteiros e realize as seguintes operações:
    . Mesclar as duas tuplas em uma única tupla;
    . Ordenar a tupla resultante em ordem crescente.
"""
def main():
    tuplas = []
    
    print("Insira números inteiros separados por ', ': \n")

    for i in range(2):
        tuplas.append(tuple(map(int,input(f'{i+1}º Tupla: ').split(', '))))
    
    newTupla = tuplas[0] + tuplas[1]
    newTuplaOrganizada = sorted(newTupla)

    print(f'1º Tupla: {tuplas[0]}'
          f'2º Tupla: {tuplas[1]}'
          f'Tupla mesclada: {newTupla}'
          f'Tupla Organizada: {newTuplaOrganizada}')
    
if __name__ == '__main__':
    main()