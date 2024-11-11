class UnavailabilityBookError(Exception):
    def __init__(self, book):
        self.message = f"Is not possible take the book: {book}"
        super().__init__(self.message)