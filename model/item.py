
class Livro():
    def __init__(self, id, book_id, id_sale, book_nome, qtd, book_valor):
        self.id = id
        self.book_id = book_id
        self.id_sale = id_sale
        self.book_nome = book_nome
        self.qtd = qtd
        self.book_valor = book_valor
    
    def getLivro(self):
        return [self.book_nome, self.qtd, self.book_valor]