from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "book.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.Text, nullable=False)
    book_publisher = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'author_name': self.author_name,
            'book_publisher': self.book_publisher
        }

@app.route('/')
def index():
    return jsonify({"message": "Books API"})

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author_name=data['author_name'],
        book_publisher=data['book_publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.book_name = data.get('book_name', book.book_name)
    book.author_name = data.get('author_name', book.author_name)
    book.book_publisher = data.get('book_publisher', book.book_publisher)
    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Delete"}), 200

if __name__ == '__main__':
    app.run(debug=True)
