from api import app, mongo
from api.models.book_model import Book
from api.services.book_service import BookService

if __name__ == '__main__':
    with app.app_context():
        if 'books' not in mongo.db.list_collection_names():
            book = Book(
                title = '',
                sinopse='',
                year = 0
            )
            BookService.add_book(book)           
    app.run(port=5000, debug=True)