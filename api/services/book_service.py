from api import mongo
from ..models import book_model
from bson import ObjectId

class BookService:
    def add_book(book):
        result = mongo.db.books.insert_one({
            'title' : book.title,
            'sinopse' : book.sinopse,
            'year' : book.year,
        })
        return mongo.db.books.find_one({'_id': ObjectId(result.inserted_id)})
        
    @staticmethod
    def get_books():
        return list(mongo.db.books.find())
    
    @staticmethod
    def get_book_by_id(id):
        return mongo.db.books.find_one({'_id' : ObjectId(id)})
    
    def update_book(self, id):
        updated_book = mongo.db.books.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set' : {
                'title' : self.title,
                'sinopse' : self.sinopse,
                'year' : self.year,
            }},
            return_document=True 
        )
        return updated_book
    
    @staticmethod
    def delete_book(id):
        mongo.db.books.delete_one({'_id' : ObjectId(id)})