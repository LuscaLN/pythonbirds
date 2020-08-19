class Pessoa:
    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'



if __name__ == '__main__':

    lucas=Pessoa(nome='Lucas')
    renato=Pessoa(lucas,nome = 'Renato', idade='43')

    print(renato.cumprimentar())
    print(renato.nome, renato.idade)
    for filho in renato.filhos:
        print(filho.nome)
