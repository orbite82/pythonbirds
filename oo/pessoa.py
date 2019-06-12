class Pessoa:
    def cuprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cuprimentar(p))
    print(id(p))
    print(p.cuprimentar())