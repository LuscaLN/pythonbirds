from unittest import TestCase
from oo.exercicio_carro import Motor

class CarroTestCase(TestCase):
    def test_de_velocidade_inicial(self):
        motor=Motor()
        self.assertEqual(0, motor.velocidade)
    def test_acelerecao(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
