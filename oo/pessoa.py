class Pessoa:
    olhos=2
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
    print(renato.nome, renato.idade, renato.olhos)
    renato.sobrenome='nogueira'
    for filho in renato.filhos:
        print(filho.nome)
    del renato.filhos
    renato.olhos=1
    print(renato.olhos, lucas.olhos)
    Pessoa.olhos=3
    print(renato.olhos, lucas.olhos)
    del renato.olhos
    print(renato.olhos)
    print(renato.__dict__)
    print(lucas.__dict__)



