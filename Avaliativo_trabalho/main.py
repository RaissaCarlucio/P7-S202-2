from pymongo import MongoClient
from MotoristaCLI import MotoristaCLI
from MotoristaDAO import MotoristaDAO
from database import Database
from collection_motoristas import inserir_motorista_com_corridas

# Fazendo a conexao e chamando algumas funcoes
db = Database(database="Avaliativo_lab1", collection="motoristas")  # Supondo que o nome da coleção seja "motoristas"
motorista_dao = MotoristaDAO(database=db)
motorista_cli = MotoristaCLI(motorista_dao)
motorista_cli.run()

#Chamando a main e suas respectivas funcoes
if __name__ == "__main__":
    db = Database(database="Avaliativo_lab1", collection="motoristas")
    motorista_dao = MotoristaDAO(database=db)
    motorista_cli = MotoristaCLI(motorista_dao)
    inserir_motorista_com_corridas()