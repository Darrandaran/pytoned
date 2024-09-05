from biblioteca import biblioteca

compra = biblioteca(livro="Jonas vai morrer",saldo=56.99)

print(compra.consultar_saldo())
compra.comprar(40)