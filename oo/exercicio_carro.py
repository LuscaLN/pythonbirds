
class carro:
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

    direcao = Direcao()

    if __name__ == '__main__':
        print(motor.velocidade)
        motor.acelerar()
        print(motor.velocidade)
        motor.acelerar()
        motor.acelerar()
        print(motor.velocidade)
        motor.frear()
        print(motor.velocidade)
        motor.frear()
        print(motor.velocidade)
        print(direcao.rumo[direcao.cont])
        direcao.virar_a_direita()
        direcao.virar_a_direita()
        print(direcao.rumo[direcao.cont])
        direcao.virar_a_direita()
        print(direcao.rumo[direcao.cont])
        direcao.virar_a_direita()
        print(direcao.rumo[direcao.cont])





