from database import Database
from teacher_crud import TeacherCRUD
from query import Query
from cli import CLI

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.207.84.251:7687", "neo4j", "bolt-mouth-glances")

# Criando uma instância da classe TeacherCRUD para interagir com o banco de dados
teacher_crud = TeacherCRUD(db)
query = Query(db)

# Questao 1 utilizando a classe Query:
#print("Buscando o nome do professor Renzo e retornando ano_nasc e cpf",query.get_renzo())
#print("\n")
#print("Buscando pelos professor cujo nome comeca com a letra M: ", query.get_Professor_letra_M())
#print("\n")
#print("Buscando o nome de todas as cidades:", query.get_todas_cidades())
#print("\n")
#print("Buscando pelas escolas, numero >=150 ou <= 550:", query.get_School())
#print("\n")

# Questao 2 utilizando a classe Query:
#print("Buscando o ano de nascimento do professor mais velho:", query.get_professor_mais_velho())
#print("\n")
#print("Buscando o ano de nascimento do professor mais jovem:", query.get_professor_mais_novo())
#print("\n")
#print("Buscando a media aritmetica dos habitantes de todas as cidades:", query.get_media_populacao())
#print("\n")
#print("Buscando a cidade cujo Cep seja igual a 37540-000:", query.get_cidade_por_cep("37540-000"))
#print("\n")
#print("Buscando o terceiro caractere em diante para todos os professores: ", query.get_terceiro_caractere_professor())
#print("\n")

# Criando o professor Chris:
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

# Pesquisando o professor Chris:
teacher_read = teacher_crud.read("Chris Lima")
print(teacher_read)

# Alterando o CPF do professor Chris:
teacher_update = teacher_crud.update("Chris Lima", "162.052.777-77")

# Realizando o CLI para criar, ler, dar update e deletar um professor da escolha do usuario: 
if __name__ == "__main__":
    cli = CLI(db)
    cli.menu()
