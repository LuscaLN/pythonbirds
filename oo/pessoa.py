class Pessoa:
    olhos=2
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

    def __init__(self,*filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 4

if __name__ == '__main__':

    lucas = Mutante(nome='Lucas')
    renato = Homem(lucas,nome = 'Renato', idade='43')

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
    print(Pessoa.metodo_estatico(), renato.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), renato.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anon')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))

    print(isinstance(renato, Pessoa))
    print(isinstance(renato, Homem))
    print(lucas.olhos)
    print(lucas.cumprimentar())
    print(renato.cumprimentar())

