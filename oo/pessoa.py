class Pessoa:
    def cumprimentar(self,nome):
        return f'Olá {nome} {id(self)}'



if __name__ == '__main__':
    p=Pessoa()
    print(p.cumprimentar('Lucas'))
