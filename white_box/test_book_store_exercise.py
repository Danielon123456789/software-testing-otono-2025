# -*- coding: utf-8 -*-

"""
Book store unit testing examples.
"""
import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore, main


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    def setUp(self):
        """
        Creates the book properties
        """
        self.title = "title"
        self.author = "author"
        self.price = 9.99
        self.quantity = 5

    def test_book_init(self):
        """
        Checks the book properties.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        self.assertEqual(book.title, self.title)
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.price, self.price)
        self.assertEqual(book.quantity, self.quantity)

    @patch("builtins.print")
    def test_book_display(self, mock_print):
        """
        Checks the book display function.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        book.display()
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call(f"Title: {self.title}")
        mock_print.assert_called_with(f"Quantity: {self.quantity}")


class TestBookStore(unittest.TestCase):
    """
    Book store unittest class.
    """

    def test_book_store_init(self):
        """
        Checks the book store properties.
        """
        book_store = BookStore()
        self.assertEqual(book_store.books, [])

    @patch("builtins.print")
    def test_add_book(self, mock_print):
        """
        Checks the add book function.
        """
        book_store = BookStore()
        book = Book("title", "author", 9.99, 5)
        book_store.add_book(book)
        self.assertIn(book, book_store.books)
        mock_print.assert_called_once_with(f"Book '{book.title}' added to the store.")

    @patch("builtins.print")
    def test_display_books_empty(self, mock_print):
        """
        Checks the display books function when no books are available.
        """
        book_store = BookStore()
        book_store.display_books()
        mock_print.assert_called_once_with("No books in the store.")

    @patch("builtins.print")
    def test_display_books_with_books(self, mock_print):
        """
        Checks the display books function when books are available.
        """
        book_store = BookStore()
        book1 = Book("title1", "author1", 9.99, 5)
        book2 = Book("title2", "author2", 19.99, 3)
        book_store.add_book(book1)
        book_store.add_book(book2)

        book_store.display_books()
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("Books available in the store:")
        self.assertEqual(
            mock_print.call_count, 11
        )  # 9 de display_books + 2 de add_book

    @patch("builtins.print")
    def test_search_book_not_found(self, mock_print):
        """
        Checks the search book function when no book is found.
        """
        book_store = BookStore()
        book_store.search_book("nonexistent")
        mock_print.assert_called_once_with("No book found with title 'nonexistent'.")

    @patch("builtins.print")
    def test_search_book_found(self, mock_print):
        """
        Checks the search book function when a book is found.
        """
        book_store = BookStore()
        book1 = Book("title1", "author1", 9.99, 5)
        book2 = Book("title2", "author2", 19.99, 3)
        book_store.add_book(book1)
        book_store.add_book(book2)

        book_store.search_book("title1")
        self.assertTrue(mock_print.called)
        mock_print.assert_any_call("Found 1 book(s) with title 'title1':")
        self.assertEqual(
            mock_print.call_count, 7
        )  # 4 de display + 2 de add_book +1 de search


class TestMainFunction(unittest.TestCase):
    """
    Tests the main() function ensuring correct input prompts and method calls.
    """

    @patch("builtins.input")
    @patch.object(BookStore, "add_book")
    @patch.object(BookStore, "display_books")
    @patch.object(BookStore, "search_book")
    def test_main_flow_with_function_calls(
        self, mock_search_book, mock_display_books, mock_add_book, mock_input
    ):
        """
        Tests that main() calls the correct methods and prompts for the correct input texts.
        """
        # Simulación de entradas del usuario
        mock_input.side_effect = [
            # Agregar un libro
            "3",  # Opción
            "The Hobbit",  # Título
            "J.R.R. Tolkien",  # Autor
            "15.5",  # Precio
            "3",  # Cantidad
            # Buscar libro
            "2",  # Opción
            "The Hobbit",  # Título buscado
            # Mostrar libros
            "1",  # Opción
            # Salir
            "4",  # Opción
        ]

        # Ejecutar la función main
        with patch("builtins.print"):  # Evita imprimir en consola real
            main()

        # Verifica que los input fueron llamados con los textos correctos
        expected_prompts = [
            "Enter your choice: ",
            "Enter the title of the book: ",
            "Enter the author of the book: ",
            "Enter the price of the book: ",
            "Enter the quantity of the book: ",
            "Enter your choice: ",
            "Enter the title of the book you want to search: ",
            "Enter your choice: ",
            "Enter your choice: ",
        ]
        actual_prompts = [call.args[0] for call in mock_input.call_args_list]
        self.assertEqual(actual_prompts, expected_prompts)

        # Verifica que se llamaron las funciones correspondientes
        self.assertTrue(mock_add_book.called)
        self.assertTrue(mock_search_book.called)
        self.assertTrue(mock_display_books.called)

        # Verifica que se llamaron exactamente una vez
        mock_add_book.assert_called_once()
        mock_search_book.assert_called_once_with("The Hobbit")
        mock_display_books.assert_called_once()
