# Library Management System

This Python script simulates a basic library management system with two main classes: `library` and `customer`. The `library` class manages a list of available books, allows customers to borrow and return books, and provides information about available books. The `customer` class represents a library user, allowing them to request and return books, and view their borrowed books.

## Usage

1. Create a library and initialize it with a list of available books:

```python
lib_cbe = library(['book1', 'book2', 'book3', 'book4', 'book5', 'book2'])
```

2. Create a customer instance:

```python
preethi = customer()
```

3. Run the script. It will display a menu of options for interacting with the library.

4. Use the menu to perform actions such as viewing available books, borrowing books, returning books, and checking the customer's borrowed books.

## Features

### `library` Class

- `show()`: Displays the list of available books in the library.

- `lend_book(book_name)`: Allows customers to borrow a book from the library. If the book is available, it is removed from the library's list, and the customer is informed that the book has been issued.

- `returnBook(book_name)`: Allows customers to return a book to the library, adding it back to the library's list.

### `customer` Class

- `add_book(book_name)`: Adds a book to the customer's list of borrowed books.

- `show()`: Displays the list of books borrowed by the customer.

- `request_book()`: Prompts the customer to enter the name of a book they wish to borrow and returns the book name.

- `return_book()`: Prompts the customer to enter the name of a book they wish to return and returns the book name.

- `lend_book_in_lib(book_name)`: Allows the customer to return a book to the library. It checks if the book is borrowed by the customer and then removes it from the customer's list and returns it to the library.

## Example

Here's an example of how to use this script:

1. Create a library instance and add a list of available books.

2. Create a customer instance.

3. Run the script.

4. Use the menu options to interact with the library, including viewing available books, borrowing books, returning books, and checking the customer's borrowed books.

## Note

This is a basic implementation for educational purposes. In a real-world scenario, you may want to consider additional features such as user authentication, a database for book records, and better error handling.
