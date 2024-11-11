class Book:
    def __init__(self, title, author, published_year, status):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.status = status
    
    def being_borrwed(self):
        self.status = "unavailability"
    
    def being_returned(self):
        self.status = "availability"
        