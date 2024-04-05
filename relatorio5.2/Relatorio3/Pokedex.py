from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self,database: Database):
        self.db = database

    def strong_against(self,name):
        fraquezas = ["Psychic", "Ice"]
        weaknesses = self.db.collection.find({"name": name}, {"weaknesses":1, "_id":0})
        strong_against = self.db.collection.find({"type": {"$in": weaknesses[0]["weaknesses"]}})
        writeAJson(strong_against, "Strong_Against_"+name+".json")
        return strong_against

    def weak_against(self, name):
        types = self.db.collection.find({"name": name}, {"type":1, "_id":0})
        weak_against = self.db.collection.find({"weaknesses": {"$all": types[0]["type"]}})
        writeAJson(weak_against, "Weak_against_" + name + ".json")
        return weak_against

    def getPokemonByName(self, name):
        pokemon_cursor = self.db.collection.find({"name": name})
        writeAJson(pokemon_cursor, "Name_" + name + ".json")
        return pokemon_cursor

    def getPokemonsByType(self, name):
        pokemon_type = self.db.collection.find({"type": {"$in": [name]}})
        writeAJson(pokemon_type, "Type_" + name + ".json")
        return pokemon_type

    def Pokemon_fraquezas(self, name):
        pokemon_fraq = self.db.collection.find({"weaknesses": {"$size": 1}})
        writeAJson(pokemon_fraq, "Type_" + name + ".json")
        return pokemon_fraq

    def Pokemon_spawn(self, name):
        pokemon_spawn = self.db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
        writeAJson(pokemon_spawn, "Type_" + name + ".json")
        return pokemon_spawn



