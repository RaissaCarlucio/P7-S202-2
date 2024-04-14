from Corrida import Corrida
class Motorista:
    def __init__(self, nota):
        self.corridas = []
        self.nota = nota
    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)
