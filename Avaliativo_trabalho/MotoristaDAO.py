
#update, create, delete

from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    # 1 - Relacao de composicao com a classe Database:
    def __init__(self, database):
        self.db = database

   # Metodos GRUD:
   # Criando o motorista
    def create_motorista(self, nome:str, nota: float):
        try:
            res = self.db.collection.insert_one({"name": nome, "nota": nota})
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None
        
    # Criando o passageiro
    def create_passageiro(self, nome:str, documento: str):
        try:
            res = self.db.collection.insert_one({"nome": nome, "documento": documento})
            print(f"Passageiro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o passageiro: {e}")
            return None
       
    # Criando uma corrida    
    def create_corrida(self, nota: float, distancia: float, valor: float):
        try:
            res = self.db.collection.insert_one({"nota": nota, "distancia": distancia, "valor": valor})
            print(f"Corrida criada com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar a corrida: {e}")
            return None

    # Método para associar passageiros a um motorista
    def associate_passageiros_to_motorista(self, motorista_id, passageiros):
        try:
            self.db.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": {"passageiros": passageiros}})
            print("Passageiros associados ao motorista.")
        except Exception as e:
            print(f"Ocorreu um erro ao associar os passageiros ao motorista: {e}")

    # Metodo para associar corridas a um motorista
    def associate_corridas_to_motorista(self, motorista_id, corridas):
        try:
            self.db.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": {"corridas": corridas}})
            print("Corridas associadas ao motorista.")
        except Exception as e:
            print(f"Ocorreu um erro ao associar as corridas ao motorista: {e}")

    # Lendo um motorista pelo seu ID
    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading person: {e}")
            return None

    # Atualizando o motorista se necessario
    def update_motorista(self, id: str, name: str, nota: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": name, "nota": nota}})
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating person: {e}")
            return None

    # Deletando o motorista
    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting person: {e}")
            return None
