class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cuprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    orbitex = Pessoa(nome='Orbitex')
    luciano = Pessoa(orbitex, nome='Luciano')
    print(Pessoa.cuprimentar(luciano))
    print(id(luciano))
    print(luciano.cuprimentar())
    print(luciano.nome)
#    luciano.nome = 'Orbite'
#    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
#    luciano.sobrenome
#    print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(orbitex.__dict__)