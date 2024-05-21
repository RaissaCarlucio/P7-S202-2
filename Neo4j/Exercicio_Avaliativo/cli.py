from teacher_crud import TeacherCRUD
# Criando a classe CLI para ajudar na classe main
class CLI:
    def __init__(self, database):
        self.teacher_crud = TeacherCRUD(database)
# Criando o menu
    def menu(self):
        print("Bem-vindo ao Menu!")
        while True:
            print("\nEscolha uma opcao:")
            print("[1] Criar professor")
            print("[2] Pesquisar professor")
            print("[3] Atualizar CPF do professor")
            print("[4] Deletar professor")
            print("[5] Sair")
            s = input("Digite o numero da opcao desejada: ")
            if s == "1":
                self.create_professor()
            elif s == "2":
                self.read_professor()
            elif s == "3":
                self.update_professor()
            elif s == "4":
                self.delete_professor()
            elif s == "5":
                print("Saindo do Menu")
                break
            else:
                print("Opção inválida. Tente novamente :( ")

# Criando as funcoes para o menu:
    def create_professor(self):
        name = input("Digite o nome do professor: ")
        ano_nasc = input("Digite o ano de nascimento do professor: ")
        cpf = input("Digite o CPF do professor: ")
        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Professor criado com sucesso :) ")

    def read_professor(self):
        name = input("Digite o nome do professor que deseja pesquisar: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print(f"Nome: {teacher['name']}")
            print(f"Ano de Nascimento: {teacher['ano_nasc']}")
            print(f"CPF: {teacher['cpf']}")
        else:
            print("Professor não encontrado :( ")

    def update_professor(self):
        name = input("Digite o nome do professor que deseja atualizar: ")
        new_cpf = input("Digite o novo CPF: ")
        self.teacher_crud.update(name, new_cpf)
        print("CPF do professor atualizado com sucesso :) ")

    def delete_professor(self):
        name = input("Digite o nome do professor que deseja deletar: ")
        if self.teacher_crud.read(name):
            self.teacher_crud.delete(name)
            if not self.teacher_crud.read(name):
                print("Professor deletado com sucesso :) ")
            else:
                print("Erro ao deletar o professor :(")
        else:
            print("Professor não encontrado.")


