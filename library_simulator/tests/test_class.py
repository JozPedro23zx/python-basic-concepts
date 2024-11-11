import pytest
# from library_simulator.classes import book as b, library as l
from ..classes.book import Book 
from ..classes.library import Library
from ..classes.member import Member

from ..exeptions.loan_limit import LoanLimitError
from ..exeptions.unavailability_book import UnavailabilityBookError
from ..exeptions.invalid_member import InvalidMemberError


member_name = "John"
title="The Lord of the Rings"
author="J.R.R. Tolkien"
published_year = 1954

member_name2 = "Steve"
title2="1984"
author2="George Orwell"
published_year2 = 1949


class TestClassCreation:
    def test_create_book(self):
        book = Book(title=title, author=author, published_year=published_year, status="availability")

        assert book.title == title
        assert book.author == author
        assert book.published_year == published_year
        assert book.status == "availability"
        
    def test_create_member(self):
        member = Member(name=member_name)

        assert member.name == member_name
        assert member.book == None

class TestLibraryFunctions:
    def test_add_book(self):
        library = Library()
        library.add_book(title=title, author=author, published_year=published_year)
            
        assert len(library.books) == 1
        assert library.books[0].title == "The Lord of the Rings"

    def test_add_member(self):
        library = Library()
        library.add_member(name=member_name)
            
        assert len(library.members) == 1
        assert library.members[0].name == member_name

    def test_lend_book(self):
        library = Library()
        library.add_book(title=title, author=author, published_year=published_year)
        library.add_member(name=member_name)

        library.lend_book(title=title, name=member_name)

        assert library.books[0].status == "unavailability"
        assert library.members[0].book == title

class TestExeptions:
    def test_loan_limit_error(self):
        library = Library()
        library.add_book(title=title, author=author, published_year=published_year)
        library.add_book(title=title2, author=author2, published_year=published_year2)
        library.add_member(name=member_name)

        library.lend_book(title=title, name=member_name)

        with pytest.raises(LoanLimitError) as err:
            library.lend_book(title=title2, name=member_name)
        assert str(err.value) == f"The member {member_name} cannot take another book"

    def test_invalid_member_error(self):
        library = Library()
        library.add_book(title=title, author=author, published_year=published_year)

        with pytest.raises(InvalidMemberError) as err:
            library.lend_book(title=title, name=member_name)
        assert str(err.value) == f"Not find any member with name: {member_name}"

    def test_unavailability_book_error(self):
        library = Library()
        library.add_book(title=title, author=author, published_year=published_year)
        library.add_member(name=member_name)
        library.add_member(name=member_name2)
        
        library.lend_book(title=title, name=member_name)

        with pytest.raises(UnavailabilityBookError) as err:
            library.lend_book(title=title, name=member_name2)
        assert str(err.value) == f"Is not possible take the book: {title}"

    def test_book_and_member_not_found(self):
        library = Library()

        with pytest.raises(InvalidMemberError) as err:
            library.lend_book(title=title, name=member_name)
        assert str(err.value) == f"Not find any member with name: {member_name}"

        library.add_member(name=member_name)

        with pytest.raises(UnavailabilityBookError) as err:
            library.lend_book(title=title, name=member_name)
        assert str(err.value) == f"Is not possible take the book: {title}"
