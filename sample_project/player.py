class Player:
    def __init__(self, name, country, score=0):
        self.name = name
        self.country = country
        self.score = score
        
    def update_score(self, score):
        self.score = self.score + score
        return True
    
    def get_score(self):
        return self.score
        
    def get_name(self):
        return self.name