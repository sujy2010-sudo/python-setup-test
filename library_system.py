# library_system.py
"""
Mini Library Management System
Week 2 - OOP & Pythonic Design
"""

import logging
from typing import List, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("library.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# --- Exceptions ---
class BookNotAvailableError(Exception):
    """Raised when trying to borrow an unavailable book"""
    pass


class DuplicateISBNError(Exception):
    """Raised when trying to add a book with an ISBN already in the library"""
    pass


class DuplicateMemberError(Exception):
    """Raised when trying to register a member with an existing member_id"""
    pass


# --- Book ---
class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available: bool = True

    # title property
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("title must be at least 2 characters")
        self._title = value.strip()

    # author property
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("author must be at least 2 characters")
        self._author = value.strip()

    # isbn property
    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, value: str):
        if not isinstance(value, str) or len(value) != 13 or not value.isdigit():
            raise ValueError("ISBN must be a 13-digit string")
        self._isbn = value

    # availability
    @property
    def available(self) -> bool:
        return self._available

    def borrow(self) -> None:
        if not self._available:
            raise BookNotAvailableError(f"Book '{self.title}' is already borrowed")
        self._available = False

    def return_book(self) -> None:
        self._available = True

    def __str__(self) -> str:
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} [{status}]"


# --- Member ---
class Member:
    def __init__(self, name: str, member_id: int, email: str) -> None:
        # uses setters for validation
        self.name = name
        self.member_id = member_id
        self.email = email
        self._borrowed_books: List[Book] = []

    # name property
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Name must be a string with at least 2 characters")
        self._name = value.strip()

    # member_id property (int)
    @property
    def member_id(self) -> int:
        return self._member_id

    @member_id.setter
    def member_id(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("member_id must be a non-negative integer")
        self._member_id = value

    # email property
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not isinstance(value, str) or "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        self._email = value.strip()

    # borrowed books (read-only copy)
    @property
    def borrowed_books(self) -> List[Book]:
        return list(self._borrowed_books)

    @property
    def books_count(self) -> int:
        return len(self._borrowed_books)

    def borrow_book(self, book: Book) -> None:
        if book in self._borrowed_books:
            logger.debug(f"Member {self.name} already has '{book.title}' recorded")
            return
        self._borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        try:
            self._borrowed_books.remove(book)
        except ValueError:
            logger.warning(f"Book '{getattr(book, 'title', str(book))}' not found in {self.name}'s borrowed list")

    def __str__(self) -> str:
        return f"Member: {self.name} (ID: {self.member_id}, Books: {self.books_count})"


# --- Library ---
class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []

    def add_book(self, book: Book) -> None:
        existing = next((b for b in self.books if b.isbn == book.isbn), None)
        if existing:
            raise DuplicateISBNError(f"ISBN {book.isbn} already exists for '{existing.title}'")
        self.books.append(book)
        logger.info(f"Added book '{book.title}' by {book.author} (ISBN: {book.isbn})")

    def register_member(self, member: Member) -> None:
        existing = next((m for m in self.members if m.member_id == member.member_id), None)
        if existing:
            raise DuplicateMemberError(f"Member ID {member.member_id} already registered for '{existing.name}'")
        self.members.append(member)
        logger.info(f"✓ Registered member: {member.name} (ID: {member.member_id})")

    def _find_book(self, isbn: str) -> Optional[Book]:
        return next((b for b in self.books if b.isbn == isbn), None)

    def _find_member(self, member_id: int) -> Optional[Member]:
        return next((m for m in self.members if m.member_id == member_id), None)

    def checkout_book(self, member_id: int, isbn: str) -> None:
        """Member borrows a book by ISBN."""
        member = self._find_member(member_id)
        if member is None:
            raise ValueError(f"Member with ID {member_id} not found")
        book = self._find_book(isbn)
        if book is None:
            raise ValueError(f"Book with ISBN {isbn} not found")
        if not book.available:
            raise BookNotAvailableError(f"Book '{book.title}' is already borrowed")

        # process checkout
        book.borrow()
        member.borrow_book(book)
        logger.info(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id: int, isbn: str) -> None:
        """Member returns a book by ISBN."""
        member = self._find_member(member_id)
        if member is None:
            raise ValueError(f"Member with ID {member_id} not found")
        book = self._find_book(isbn)
        if book is None:
            raise ValueError(f"Book with ISBN {isbn} not found")

        # process return
        book.return_book()
        member.return_book(book)
        logger.info(f"{member.name} returned '{book.title}'")

    def get_available_books(self) -> List[Book]:
        return [book for book in self.books if book.available]

    def get_borrowed_books(self) -> List[Book]:
        return [book for book in self.books if not book.available]

    def generate_report(self) -> None:
        """Generate and log a summary report of the library state."""
        total_books = len(self.books)
        available_books = len(self.get_available_books())
        borrowed_books = len(self.get_borrowed_books())
        total_members = len(self.members)

        logger.info("=" * 80)
        logger.info("📊 LIBRARY REPORT")
        logger.info("=" * 80)
        logger.info(f"Total Books: {total_books}")
        logger.info(f"Available Books: {available_books}")
        logger.info(f"Borrowed Books: {borrowed_books}")
        logger.info(f"Total Members: {total_members}")

        if borrowed_books:
            logger.info("\nCurrently Borrowed Books:")
            for book in self.get_borrowed_books():
                borrower = next((m for m in self.members if book in m._borrowed_books), None)
                if borrower:
                    logger.info(f" • {book.title} by {book.author} - borrowed by {borrower.name}")
                else:
                    logger.info(f" • {book.title} by {book.author} - borrower unknown")
        else:
            logger.info("\nCurrently Borrowed Books: None")

        logger.info("\nAvailable Books:")
        for book in self.get_available_books():
            logger.info(f" • {book.title} by {book.author}")

        logger.info("\nMembers:")
        for member in self.members:
            logger.info(f" • {member.name} (ID: {member.member_id}) - {member.books_count} book(s) borrowed")

        logger.info("=" * 80)


# --- Demo / Tests ---
def main():
    print("=" * 80)
    print("📚 CITY LIBRARY MANAGEMENT SYSTEM")
    print("=" * 80)

    library = Library("City Library")

    # Create books
    try:
        book1 = Book("Python Crash Course", "Eric Matthes", "9781593279288")
        book2 = Book("Clean Code", "Robert Martin", "9780132350884")
        book3 = Book("Pragmatic Programmer", "Andy Hunt", "9780135957059")
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
    except Exception as e:
        logger.error(f"✗ Error adding book: {e}")

    # Register members
    try:
        alice = Member("Alice Johnson", 1001, "alice@example.com")
        bob = Member("Bob Smith", 1002, "bob.smith@example.com")
        library.register_member(alice)
        library.register_member(bob)
    except Exception as e:
        logger.error(f"✗ Error registering member: {e}")

    # Borrow books
    try:
        library.checkout_book(1002, "9781593279288")  # Bob borrows Python
        library.checkout_book(1001, "9780132350884")  # Alice borrows Clean Code
    except Exception as e:
        logger.error(f"✗ Checkout error: {e}")

    # Try to borrow already borrowed book (should fail)
    try:
        library.checkout_book(1002, "9780132350884")  # Bob tries Clean Code
    except BookNotAvailableError as e:
        logger.error(str(e))

    # Return a book
    try:
        library.return_book(1002, "9781593279288")  # Bob returns Python
    except Exception as e:
        logger.error(f"✗ Return error: {e}")

    # Generate report
    library.generate_report()

    print("=" * 80)


if __name__ == "__main__":
    main()
