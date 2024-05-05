class FutebolDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (:Player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)    

    def create_match(self, match_id, result, player_ids):
        query = "CREATE (:Match {id: $match_id, result: $result})"
        parameters = {"match_id": match_id, "result": result}
        self.db.execute_query(query, parameters)
        
        for player_id in player_ids:
            query = """
            MATCH (m:Match {id:$match_id}) MATCH (p:Player {id: $player_id}) CREATE (m) - [:PARTICIPANTES_JOGO] -> (p)
            """
            parameters = {"match_id": match_id, "player_id": player_id}
            self.db.execute_query(query, parameters)

    #-----------------------------------------
    
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [(result["id"], result["name"]) for result in results]

    def get_matchs(self):
        query = "MATCH (m:Match) RETURN m.id AS MatchId, m.result AS result"
        results = self.db.execute_query(query)
        return [(result["MatchId"], result["result"]) for result in results]
    
    #-----------------------------------------

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id, name):
        query = "MATCH (p:Player {id: $player_id, name: $name}) DETACH DELETE p"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)
