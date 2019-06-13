class Pessoa:
    def __init__(self, nome=None, idadde=35):
        self.idadde = idadde
        self.nome = nome

    def cuprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    p = Pessoa('Luciene')
    print(Pessoa.cuprimentar(p))
    print(id(p))
    print(p.cuprimentar())
    print(p.nome)
    p.nome = 'Orbite'
    print(p.nome)
    print(p.idadde)






















