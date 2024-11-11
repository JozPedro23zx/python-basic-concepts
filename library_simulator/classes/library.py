from ..exeptions.unavailability_book import UnavailabilityBookError
from ..exeptions.invalid_member import InvalidMemberError
from ..exeptions.loan_limit import LoanLimitError
from .book import Book
from .member import Member

class Library:
    def __init__(self):
        self.books  = []
        self.members = []

    def add_book(self, title, author, published_year, status = "availability"):
        self.books.append(Book(title, author, published_year, status))
        
    def add_member(self, name):
        self.members.append(Member(name))


    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def remove_member(self, name):
        for member in self.member:
            if member.name == name:
                self.members.remove(member)


    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def find_all_book(self):
        return self.books
    

    def find_member(self, title):
        for member in self.members:
            if member.title == title:
                return member

    def find_all_member(self):
        return self.members


    
    def lend_book(self, title, name):
        bookFound = False
        memberFound = False
        try:
            for member in self.members:
                if member.name == name:
                    if member.book == None:
                        memberFound = True
                        break 
                    else:
                        raise LoanLimitError(name)
            if memberFound == False:
                raise InvalidMemberError(name)
                    
            for book in self.books:
                if book.title == title:
                    if book.status == "availability":
                        book.being_borrwed()
                        member.take_book(title)
                        bookFound = True
                        break
                    else:
                        raise UnavailabilityBookError(title)
            if bookFound == False:
                raise UnavailabilityBookError(title) 
        except InvalidMemberError as err:
            print(err)
            raise
        except LoanLimitError as err:
            print(err)
            raise
        except UnavailabilityBookError as err:
            print(err)
            raise
    
    def return_book(self, title, name):
        bookFound = False
        memberFound = False

        try:
            for member in self.members:
                if member.name == name:
                    member.giveback_book()
                    memberFound = True
                    break
            if memberFound == False:
                InvalidMemberError(name)
            
            for book in self.books:
                if book.title == title:
                    book.being_returned()
                    bookFound = True
                    break
            if bookFound == False:
                UnavailabilityBookError(title) 
        except InvalidMemberError as err:
            print(err)
        except UnavailabilityBookError as err:
            print(err)