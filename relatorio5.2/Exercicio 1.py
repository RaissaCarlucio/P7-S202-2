#Exercício 1:
class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}.'

#Verificando para ver se o Exercício está correto    
professor = Professor('Jonas')
mensagem1 = professor.ministrar_aula('Python')
print(mensagem1)

print("\n")
print('--------------------Ex2--------------------')

#Exercicio 2:
class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        return f'O Aluno {self.nome} está presente.'

#Verificando para ver se o Exercício está correto    
aluno = Aluno('Leonardo')
mensagem2 = aluno.presenca()
print(mensagem2)

print("\n")
print('--------------------Ex3--------------------')

#Exercicio3:
class Aluno3:
    def __init__(self, nome_aluno):
        self.nome_aluno = nome_aluno

    def presenca3(self):
        return f'O Aluno {self.nome_aluno} está presente.'

class Professor3:
    def __init__(self, nome_prof):
        self.nome_prof = nome_prof

class Aula:
    def __init__(self, professor3, assunto):
        self.professor3 = professor3
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def lista_presenca(self):
        frase = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor3.nome_prof}.\n'
        for aluno in self.alunos:
            frase += f"O aluno {aluno.nome_aluno} está presente.\n"
        return frase

professor = Professor3("Lucas")
aluno1 = Aluno3("Maria")
aluno2 = Aluno3("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.lista_presenca())
    