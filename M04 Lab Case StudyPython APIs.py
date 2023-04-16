from flask import Flask, jsonify, request

app = Flask(__name__)

# create an array to store books
books = [
  {
    'id': 1,
    'book_name': 'The Alchemist',
    'author': 'Paulo Coelho',
    'publisher': 'HarperCollins'
  },
  {
    'id': 2,
    'book_name': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'publisher': 'J. B. Lippincott & Co.'
  }
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
  return jsonify(books)

# GET a book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
  book = next((book for book in books if book['id'] == id), None)
  if book is None:
    return jsonify({'error': 'Book not found'}), 404
  return jsonify(book)

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
  new_book = {
    'id': len(books) + 1,
    'book_name': request.json['book_name'],
    'author': request.json['author'],
    'publisher': request.json['publisher']
  }
  books.append(new_book)
  return jsonify(new_book), 201

# PUT update a book by id
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
  book = next((book for book in books if book['id'] == id), None)
  if book is None:
    return jsonify({'error': 'Book not found'}), 404
  book['book_name'] = request.json['book_name']
  book['author'] = request.json['author']
  book['publisher'] = request.json['publisher']
  return jsonify(book)

# DELETE a book by id
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
  book = next((book for book in books if book['id'] == id), None)
  if book is None:
    return jsonify({'error': 'Book not found'}), 404
  books.remove(book)
  return '', 204

if __name__ == '__main__':
  app.run(debug=True)
