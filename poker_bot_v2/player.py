from medals import Medals

class Player:
    def __init__(self, id:str|None, key:str, rating:int, medals:Medals):
        self.id = id
        self.key = key
        self.rating = rating
        self.medals = medals

    def get_name(self) -> str:
        return self.id if (type(self.id) != None) else self.key

    def get_data(self) -> dict:
        obj:dict = {}
        obj['id']:str = self.id if (type(self.id) != None) else None
        obj['key']:str = self.key
        obj['rating']:int = self.rating
        obj['medals']:Medals = self.medals.get_data()
        return obj
    
    def set_id(self, id:str):
        self.id = id
    
    def set_rating(self, rating:str):
        self.rating = rating
