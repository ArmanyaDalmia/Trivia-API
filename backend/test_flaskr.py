import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('armanyadalmia', 'armanyadalmia','localhost:5433', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        # self.assertTrue(len(data['books']))



    # def test_get_paginated_books(self):
    #     res = self.client().get('/books')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))

    # def test_404_sent_requesting_beyond_valid_page(self):
    #     res = self.client().get('/books?page=1000', json={'rating': 1})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'resource not found')

    # def test_get_book_search_with_result(self):
    #     res = self.client().get('/books', json={'search': 'Brisingr'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_books'])
    #     self.assertEqual(len(data['books']), 5)

    # def test_get_book_search_without_result(self):
    #     res = self.client().get('/books', json={'search': 'something'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_books'], 0)
    #     self.assertEqual(len(data['books']), 0)

    # def test_update_book_rating(self):
    #     res = self.client().patch('/books/4', json={'rating': 2})
    #     data = json.loads(res.data)
    #     book = Book.query.filter(Book.id == 4).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(book.format()['rating'], 2)

    # def test_400_for_failed_update(self):
    #     res = self.client().patch('/books/1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'bad request')

    # def test_delete_book(self):
    #     res = self.client().delete('/books/3')
    #     data = json.loads(res.data)

    #     book = Book.query.filter(Book.id == 3).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 3)
    #     self.assertTrue(data['total_books'])
    #     self.assertTrue(len(data['books']))
    #     self.assertEqual(book, None)

    # def test_404_if_book_does_not_exist(self):
    #     res = self.client().delete('/books/1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'unprocessable')

    # def test_create_new_book(self):
    #     res = self.client().post('/books', json=self.new_book)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])
    #     self.assertTrue(len(data['books']))

    # def test_405_if_book_creation_not_allowed(self):
    #     res = self.client().post('/books/45', json=self.new_book)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'method not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()