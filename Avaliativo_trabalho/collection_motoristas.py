def inserir_motorista_com_corridas():
    db = Database(database="Avaliativo_lab1", collection="motoristas")
    documento_motorista = {
        "nome": "Raissa",
        "corridas": []
    }

    # Add required fields for a corrida
    corrida1 = {
        "nota": 10,
        "distancia": 20,
        "valor": 30,
        "passageiro": {
            "nome": "João",
            "documento": 123456
        }
    }

    # Add required fields for a corrida
    corrida2 = {
        "nota": 8,
        "distancia": 15,
        "valor": 25,
        "passageiro": {
            "nome": "Maria",
            "documento": 789012
        }
    }
    try:
        db.collection.validate(dumps(documento_motorista))
        db.collection.insert_one(documento_motorista)
        print("Motorista inserido com sucesso!")
    except ValidationError as e:
        print("Erro ao validar o documento:", e.message)
