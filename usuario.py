class Usuario:
    def __init__(self, nome, sobrenome, trabalho, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.trabalho = trabalho
        self.endereco = endereco

    @property
    def mostra_nome(self):
        return self.nome +' '+ self.sobrenome

    @property
    def mostra_emprego(self):
        return self.nome +' é '+ self.endereco

    @property
    def mostra_endereco(self):
        return self.nome +' mora em: '+ self.endereco
