class controle:
    def __init__(self, codigo, quantidade, valor ):
        self.codigo = codigo 
        self.quantidade = quantidade 
        self.valor = valor 

    def remover_produto(self):
        return f"remover produto; {self.codigo}"

    def comprar(self,valor):
        if valor >= 0:
            if self.quantidade >= valor:
                