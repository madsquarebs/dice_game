import logging

class Player:
    logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('Player')
    def __init__(self, name, country, score=0):
        self.name = name
        self.country = country
        self.score = score
        
    def update_score(self, score):
        self.score = self.score + score
        logger.info(f"Updated player score is: {self.score}")
        return True
    
    def get_score(self):
        return self.score
        
    def get_name(self):
        return self.name
