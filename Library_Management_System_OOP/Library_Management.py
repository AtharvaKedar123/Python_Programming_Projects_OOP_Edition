class Book:
    def __init__(self, book_id, title, copies):
        self.book_id = book_id
        self.title = title
        self.available_copies = copies

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def check_availability(self):
        return self.available_copies > 0

    def update_copies(self, count):
        self.available_copies += count


class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.borrowed_books = []

    def get_member_id(self):
        return self.member_id

    def get_member_name(self):
        return self.member_name

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            return -1
        if book.check_availability():
            self.borrowed_books.append(book)
            return True
        else:
            return -1

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        else:
            return -1



class Library:
    def __init__(self, library_name):
        self.library_name = library_name

    def issue_book(self, member, book):
        borrow_result = member.borrow_book(book)
        if borrow_result == True:
            book.update_copies(-1)
            return "Book issued successfully"
        else:
            return -1

    def accept_return(self, member, book):
        return_result = member.return_book(book)
        if return_result == True:
            book.update_copies(1)
            return "Book returned successfully"
        else:
            return -1
        

b1 = Book("B101", "Python Programming", 5)
b2 = Book("B102", "Data Science", 2)
b3 = Book("B103", "Machine Learning", 0)  


m1 = Member(201, "Alice")


lib = Library("LibraTech")


print(lib.issue_book(m1, b1))  
print(lib.issue_book(m1, b2))   
print(lib.issue_book(m1, b3))  
print(lib.issue_book(m1, b1))   
print(lib.issue_book(m1, b2))   


print(lib.accept_return(m1, b1)) 
print(lib.accept_return(m1, b1)) 
print(lib.accept_return(m1, b3)) 


print(b1.get_title(), "Available Copies:", b1.available_copies)  
print(b3.get_title(), "Available Copies:", b3.available_copies)  
