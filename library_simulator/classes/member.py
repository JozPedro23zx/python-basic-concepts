class Member:
    def __init__(self, name):
        self.name = name
        self.book = None
    
    def take_book(self, book):
        self.book = book

    def giveback_book(self, book):
        if book == self.book:
            self.book = None