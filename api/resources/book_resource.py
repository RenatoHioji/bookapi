from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import book_schema
from ..models import book_model
from ..services.book_service import BookService

class Books(Resource):
    def get(self):
        books = BookService.get_books()
        book = book_schema.BookSchema(many=True)
        return make_response(book.jsonify(books), 200)
    
    def post(self):
        bookschema = book_schema.BookSchema()
        validate = bookschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_book = book_model.Book(**json_data)
            result = BookService.add_book(new_book)
            res = bookschema.jsonify(result)
            return make_response(res, 201) 
        
class BookDetail(Resource):
    def get(self, id):
        book = BookService.get_book_by_id(id)
        if book is None:
            return make_response(jsonify("Livro não encontrado."), 400)
        bookschema = book_schema.BookSchema()
        return make_response(bookschema.jsonify(book), 200) 
    
    def put(self, id):
        book_existed = BookService.get_game_by_id(id)
        if book_existed is None:
            return make_response(jsonify("Livro não foi encontrado."), 404)
        bookschema = book_schema.BookSchema()
        validate = bookschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_book = book_model.Book(**json_data)
            updated_book = GameService.update_book(new_book, id)
            return make_response(bookschema.jsonify(updated_book), 200)
        
    def delete(self, id):
        book_existed = BookService.get_book_by_id(id)
        if book_existed is None:
            return make_response(jsonify("Livro não encontrado."), 404)
        BookService.delete_book(id)
        return make_response(jsonify("Livro excluído com sucesso!"), 200)


api.add_resource(Books, '/books')
api.add_resource(BookDetail, '/book/<id>')
