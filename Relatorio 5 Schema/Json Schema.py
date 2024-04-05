# Criando schemas para o MongDB, nao vai ser necessario rodar aqui no vs code esse:

# Crie uma collection Livros com uma validation (schema) que aprove os seguintes documentos JSON:


[
  {
    "_id": 1,
    "titulo": "Clean Code",
    "autor": "Robert C. Martin",
    "ano": 2008,
    "preco": 31.0
    
  }, 
  {
    "_id": "2,
    "titulo": "Harry Potter and the Philosopher's Stone",
    "autor": "J.K. Rowling",
    "ano": 1997,
    "preco": 31.0,
  }, 
]

{
    $jsonSchema: {
        bsonType: 'object',
        required: [
            'id',
            'titulo',
            'autor',
            'ano',
            'preco'
        ],
        properties: {
            id: {
                bsonType: 'int',
                description: 'deve ser um inteirno e é obrigatório'
            },
            titulo: {
                bsonType: 'string',
                description: 'deve ser uma string e é obrigatória'
            },
            autor: {
                bsonType: 'string'
                description: 'deve ser uma string e é obrigatória'
            },
            ano: {
                bsonType: 'int'
                minimum: 1900,
                maximum: 2024,
                description: 'deve ser um inteiro entre [1900, 2024] e é obrigatório' 
            }
            preco: {
                    bsonType: [
                    'double',
                    'int'
                ],
                    description: 'deve ser um double' 
            }
            
        }
             
    }
      
}

