from api import mongo

class Book():
    def __init__(self, title, sinopse, year):
        self.title = title
        self.sinopse = sinopse
        self.year = year