from database import Database
from personModel import PersonModel
from pymongo import MongoClient

db = Database(database="relatorio_5", collection="pessoas")
personModel = PersonModel(database=db)

# Função para criar a coleção de livros no mongdb
def create_livros_no_mongdb(database):
    try:
        collection_names = database.list_collection_names()
        if "livros" not in collection_names:
            database.create_collection("livros")
            print("Coleção 'livros' criada com sucesso!")
        else:
            print("A coleção 'livros' já existe.")
    except Exception as e:
        print(f"Erro ao criar coleção 'livros': {e}")

# Conectar ao banco de dados Mongo
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["relatorio_5"]
    create_livros_no_mongdb(db)
except Exception as e:
    print(f"Erro ao conectar ao banco de dados MongoDB: {e}")

# Fazendo o menu
def menu():
    print("Menu:")
    print("1 - criar um usuario")
    print("2 - Ler a pessoa por um ID")
    print("3 - Update")
    print("4 - Delete")
    print("5 - Sair")

def create1():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa"))
    x = personModel.create_person(nome,idade)
    print(x)

def read():
    id = input("Digite o ID da pessoa: ")
    y = personModel.read_person_by_id(id)
    print(y)

def update():
    id = input("Digite o ID da pessoa que deseja atualizar: ")
    novo_nome = input("Digite o novo nome: ")
    nova_idade = int(input("Digite a nova idade: "))
    z = personModel.update_person(id, novo_nome, nova_idade)
    print(z)


def delete():
    delete_id = input("ID que deseja deletar: ")
    w = personModel.delete_person_by_id(delete_id)
    print(w)

menu()

while True:
    choice = input("Escolha uma opção: ")
    if choice == "1":
        create1()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        print("Saindo do menu")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

