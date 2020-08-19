class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'



if __name__ == '__main__':
    p=Pessoa(idade='18')
    print(p.cumprimentar())
    print(p.nome, p.idade)
    p.nome='Lucas'
    print(p.nome)