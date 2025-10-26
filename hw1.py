class Book:
    def __init__(self, title, authors, publication_year,):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year

    def __str__(self):
        auth = ' & '.join(self.authors)
        return f'{auth}: {self.title} ({self.publication_year})'

    def num_authors(self):
        return len(self.authors)

books = [
    Book('Introduction to Algorithms (3rd ed.)',
            ['Cormen', 'Leiserson', 'Rivest', 'Stein'],
            2009),
    Book('ABC', ['P', 'J'], 2008),
    Book('6767', ['6', '7', 'KI'], 1967)
]
def get_num_authors(book):
    return book.num_authors()

books.sort(key=get_num_authors, reverse=True)

for x in books:
    print(x)