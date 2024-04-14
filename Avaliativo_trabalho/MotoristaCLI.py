from SimpleCLI import SimpleCLI

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    # Metodo para criar um motorista, um passageiro e uma corrida.
    def create_motorista(self):
        nome = input("Informe o nome do motorista: ")
        nota = float(input("Informe a nota do motorista: "))

        motorista_id = self.motorista_dao.create_motorista(nome, nota)

        if motorista_id:
            # Criando passageiros
            num_passageiros = int(input("Informe o número de passageiros: "))
            passageiros = []
            for _ in range(num_passageiros):
                nome_passageiro = input("Informe o nome do passageiro: ")
                documento_passageiro = input("Informe o documento do passageiro: ")
                passageiro_id = self.motorista_dao.create_passageiro(nome_passageiro, documento_passageiro)
                passageiros.append(passageiro_id)

            # Criando corridas
            num_corridas = int(input("Informe o número de corridas: "))
            corridas = []
            for _ in range(num_corridas):
                nota_corrida = float(input("Informe a nota da corrida: "))
                distancia_corrida = float(input("Informe a distância da corrida: "))
                valor_corrida = float(input("Informe o valor da corrida: "))
                corrida_id = self.motorista_dao.create_corrida(nota_corrida, distancia_corrida, valor_corrida)
                corridas.append(corrida_id)

            # Associando passageiros e corridas ao motorista
            self.motorista_dao.associate_passageiros_to_motorista(motorista_id, passageiros)
            self.motorista_dao.associate_corridas_to_motorista(motorista_id, corridas)

            print("Motorista, passageiros e corridas criados com sucesso.")

    # Lendo o motorista
    def read_motorista(self):
        id = input("Informe o ID do motorista: ")
        self.motorista_dao.read_motorista_by_id(id)

    # Atualizando as informacoes do motorista caso necessario
    def update_motorista(self):
        id = input("Informe o ID do motorista: ")
        nome = input("Informe o novo nome do motorista: ")
        nota = float(input("Informe a nova nota do motorista: "))
        self.motorista_dao.update_motorista(id, nome, nota)

    # Deletando o motorista
    def delete_motorista(self):
        id = input("Informe o ID do motorista que deseja excluir: ")
        self.motorista_dao.delete_motorista(id)
        
        # Metodo de menu que ira aparecer no terminal para o usuario realizar a entrada de dados.
    def run(self):
        print("Iniciando o programa")
        try:
            print("Bem-vindo!")
            print("Escolha alguns comandos que estão disponíveis: create, read, update, delete, quit")

            while True:
                command = input("Entre com um comando: ")
                if command == "quit" or command == "exit":  # Adicionando "exit" como outro comando de saída
                    print("Você saiu do menu")
                    return
                elif command == "create":
                    self.create_motorista()
                elif command == "read":
                    self.read_motorista()
                elif command == "update":
                    self.update_motorista()
                elif command == "delete":
                    self.delete_motorista()
                else:
                    print("Comando inválido, digite novamente.")
        except Exception as e:
            print(f"Erro: {e}")
