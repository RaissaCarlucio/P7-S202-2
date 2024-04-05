from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

# 1 - Retorne o total de vendas por dia.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {
        "_id": "$data_compra",
        "total_vendas": {"$sum": "$produtos.quantidade"}
    }}
])
writeAJson(result, "Total de vendas por dia")

# 2 - Retorne o produto mais vendido em todas as compras.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$data_compra",
                "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
])
writeAJson(result, "Produto mais vendido")

#3 - Encontre o cliente que mais gastou em uma única compra.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {
        "_id": "$cliente_id",
        "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
    }},
    {"$sort": {"total_gasto": -1}},  # Ordena os resultados em ordem decrescente pelo total gasto
    {"$limit": 1}  # Limita o resultado a apenas o cliente que gastou mais
])
writeAJson(result, "Cliente que mais gastou em uma unica compra")

# 4 - Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$match": {
        "produtos.quantidade": {"$gt": 1}
    }},
    {"$group": {
       "_id": "$produtos.descricao"
    }}
])
writeAJson(result, "Produtos com quantidade vendida acima de 1 unidade")


