"""
Crie uma classe Biblioteca para compra de livros
Atributos da classe: Livro, coleção, saldo (valor 1 ponto)

Métodos
Comprar
(comprar livro ou coleção, informar o valor e diminuir do saldo do caixa)(valor 1 ponto)

Instancie um objeto desta classe (valor 1 ponto)
"""
class biblioteca:
    def __init__(self, livro, colecao="nenhum", saldo = 300.0):
        self.nome = livro
        self.colecao = colecao
        self.saldo = saldo
    
    def consultar_saldo(self):
        return f"Saldo do caixa: {self.saldo}"
    
    def comprar(self,valor):
        if valor >= 0:
            if self.saldo >= valor:
                self.saldo -= valor
                return print(f"Compra de '{self.nome}' realizada com sucesso!!")
            else:
                return print(f"Saldo insuficiente, saldo atual: {self.saldo}")
        else:
            return "Valor inválido"