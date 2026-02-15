\## Problem Statement



LibraTech, a digital library, wants to automate the process of issuing books to its members and tracking borrowed books. The system should allow members to borrow and return books while maintaining availability counts.  



You are required to implement this system using Python \*\*OOP concepts\*\*, following the class diagram and rules provided.



---



\## Class Diagram



&nbsp;                 +-------------------------------+

&nbsp;                 |             Book              |

&nbsp;                 +-------------------------------+

&nbsp;                 | - book\_id : str               |

&nbsp;                 | - title : str                 |

&nbsp;                 | - available\_copies : int      |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(book\_id, title, copies) |

&nbsp;                 | + get\_book\_id() : str         |

&nbsp;                 | + get\_title() : str           |

&nbsp;                 | + check\_availability() : bool|

&nbsp;                 | + update\_copies(count)        |

&nbsp;                 +-------------------------------+



&nbsp;                        1

&nbsp;                        |

&nbsp;                        | Aggregation (Has-A)

&nbsp;                        ◇

&nbsp;                        |

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |            Member             |

&nbsp;                 +-------------------------------+

&nbsp;                 | - member\_id : int             |

&nbsp;                 | - member\_name : str           |

&nbsp;                 | - borrowed\_books : list       |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(id, name)          |

&nbsp;                 | + get\_member\_id() : int       |

&nbsp;                 | + get\_member\_name() : str     |

&nbsp;                 | + borrow\_book(book)           |

&nbsp;                 | + return\_book(book)           |

&nbsp;                 +-------------------------------+



&nbsp;                        ^

&nbsp;                        |

&nbsp;                        | Association (Uses)

&nbsp;                        |

&nbsp;                 +-------------------------------+

&nbsp;                 |          Library              |

&nbsp;                 +-------------------------------+

&nbsp;                 | - library\_name : str          |

&nbsp;                 +-------------------------------+

&nbsp;                 | + \_\_init\_\_(name)              |

&nbsp;                 | + issue\_book(member, book)    |

&nbsp;                 | + accept\_return(member, book) |

&nbsp;                 +-------------------------------+





---



\## Class Descriptions



\### Book Class



\*\*Attributes:\*\*

\- `book\_id` – Unique identifier of the book.  

\- `title` – Name of the book.  

\- `available\_copies` – Number of copies available for borrowing.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(book\_id, title, copies)` – Initializes the book details.  

2\. `get\_book\_id()` – Returns the book’s ID.  

3\. `get\_title()` – Returns the title of the book.  

4\. `check\_availability()` – Returns `True` if `available\_copies > 0`, else `False`.  

5\. `update\_copies(count)` – Adds or subtracts copies (e.g., after borrowing or return).  



---



\### Member Class



\*\*Attributes:\*\*

\- `member\_id` – Unique identifier of the member.  

\- `member\_name` – Name of the member.  

\- `borrowed\_books` – List of Book objects borrowed by the member.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, name)` – Initializes member details and empty `borrowed\_books`.  

2\. `get\_member\_id()` – Returns member ID.  

3\. `get\_member\_name()` – Returns member name.  

4\. `borrow\_book(book)` – Adds the book to `borrowed\_books` if member has less than 3 books and the book is available.  

5\. `return\_book(book)` – Removes the book from `borrowed\_books`.  



---



\### Library Class



\*\*Attributes:\*\*

\- `library\_name` – Name of the library.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(name)` – Initializes library name.  

2\. `issue\_book(member, book)` – Issues a book to a member if:  

&nbsp;  - Member has less than 3 borrowed books.  

&nbsp;  - Book is available (`available\_copies > 0`).  

&nbsp;  - If successful, decrease `available\_copies` by 1 and add book to member’s borrowed list.  

&nbsp;  - Returns `"Book issued successfully"` or `-1` if validation fails.  

3\. `accept\_return(member, book)` – Accepts the return of a book:  

&nbsp;  - Removes the book from member’s borrowed list.  

&nbsp;  - Increases `available\_copies` by 1.  

&nbsp;  - Returns `"Book returned successfully"` or `-1` if the book was not borrowed.  



---



\## Rules and Constraints



1\. Each member \*\*cannot borrow more than 3 books at a time\*\*.  

2\. Books \*\*cannot be issued\*\* if `available\_copies = 0`.  

3\. A book can be returned \*\*only if the member has borrowed it\*\*.  

4\. All validations must be strictly followed.  

5\. Use \*\*aggregation\*\* between Member and Book.  

6\. Library uses association to handle Members and Books.  



---



\## Expected Behavior



| Scenario | Output |

|----------|--------|

| Successful borrow | `"Book issued successfully"` |

| Borrowing more than 3 books | `-1` |

| Borrowing unavailable book | `-1` |

| Successful return | `"Book returned successfully"` |

| Returning a book not borrowed | `-1` |



---



\## Sample Usage



```python

\# Create Book objects

b1 = Book("B101", "Python Programming", 5)

b2 = Book("B102", "Data Science", 2)

b3 = Book("B103", "Machine Learning", 0)  # unavailable book



\# Create Member object

m1 = Member(201, "Alice")



\# Create Library object

lib = Library("LibraTech")



\# Issue books

print(lib.issue\_book(m1, b1))   # Book issued successfully

print(lib.issue\_book(m1, b2))   # Book issued successfully

print(lib.issue\_book(m1, b3))   # -1 (unavailable)

print(lib.issue\_book(m1, b1))   # Book issued successfully

print(lib.issue\_book(m1, b2))   # -1 (already 3 books borrowed)



\# Return books

print(lib.accept\_return(m1, b1)) # Book returned successfully

print(lib.accept\_return(m1, b1)) # -1 (already returned)

print(lib.accept\_return(m1, b3)) # -1 (never borrowed)



\# Check book availability

print(b1.get\_title(), "Available Copies:", b1.available\_copies)  # Python Programming Available Copies: 3

print(b3.get\_title(), "Available Copies:", b3.available\_copies)  # Machine Learning Available Copies: 0

