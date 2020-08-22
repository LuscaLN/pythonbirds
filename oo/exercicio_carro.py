
class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao
    def calc_vel(self):
        return self.motor.velocidade
    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()
    def sentido(self):
        return self.direcao.rumo[self.direcao.cont]
    def direita(self):
        self.direcao.virar_a_direita()
    def esquerda(self):
        self.direcao.virar_a_esquerda()

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = self.velocidade+1
    def frear(self):
        if(self.velocidade>=2):
            self.velocidade=self.velocidade-2
        else:
            self.velocidade=0


motor = Motor(velocidade=0)

class Direcao:
    def __init__(self, rumo=['Norte', 'Leste', 'Sul', 'Oeste'], cont=0):
        self.rumo = rumo
        self.cont = cont
    def virar_a_direita(self):
        if self.cont < 3:
            self.cont = self.cont+1
        else:
            self.cont = 0
    def virar_a_esquerda(self):
        if self.cont == 0:
            self.cont = 3
        else:
            self.cont = self.cont-1



direcao = Direcao()
carro = Carro(motor, direcao)

if __name__ == '__main__':
    print(carro.calc_vel())
    carro.acelerar()
    carro.acelerar()
    carro.acelerar()
    print(carro.calc_vel())
    print(carro.sentido())





