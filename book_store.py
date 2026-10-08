class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2026 - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)

print(book.get_age())
print(book.get_summary())