def get_book_categoria(lista):
    match lista:
        case '1':
            return "ficção"
        case '2':
            return "romance"
        case '3':
            return "terror"
        case '4':
            return "suspense"
        case '5':
            return "comédia"
        
# Exemplo de uso
category_list = []

# Simulando a adição de categoria à lista
for code in ['1','4','5','2']:
    category = get_book_categoria(code)
    category_list.append(category)

print(category_list)