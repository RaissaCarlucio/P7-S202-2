from database import Database
from helper.writeAJson import writeAJson
from Pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(db)

pokedex.strong_against("Charmander")
pokedex.weak_against("Kakuna")
pokedex.getPokemonByName("Bulbasaur")
pokedex.getPokemonsByType("Fire")
pokedex.Pokemon_fraquezas("Electric")
pokedex.Pokemon_spawn("Charmander")