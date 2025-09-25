def string_reverse(string):
    return string[::-1]
# string_reverse()
def even_sum(lis):
    sum = 0
    for i in lis:
        if i%2==0:
            sum +=i
    return sum
print(even_sum([1,2,3,4,5,6]))
# first unique character in a string
def unique_character(s):
    unique_char = {}
    unique_char_list = []
    for i in s:
        if i in unique_char:
            unique_char[i]+=1
        else:
            unique_char[i]=1
    for i in unique_char:
        if unique_char[i] ==1:
            unique_char_list.append(i)
    return unique_char_list[0]



# print(unique_character('aabccdee'))


# Fibonacci NumberWrite a function that returns the nth Fibonacci number. Assume the first two Fibonacci numbers are 0 and 1.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    series = [0,1]
    for k in range(2, n):
        next_val = series[-1] + series[-2]  
        series.append(next_val)
    return series

print(fibonacci(6))

"""
Write a function in Python or Java that:
 - Takes a list of integers as input (API IDs)
 - Returns only unique IDs, sorted
 - Include a unit test for your function
 Example: Input: [5, 2, 9, 5, 1, 2] → Output: [1, 2, 5, 9]
 """


def unique_sorted_list(lis):
    new_lis =  []
    for i in lis:
        if i not in new_lis:
            new_lis.append(i)
    n = len(new_lis)
    for i in range(n):
        for j in range(0, n-i-1):
            if new_lis[j] > new_lis[j+1]:
                new_lis[j], new_lis[j+1] = new_lis[j+1], new_lis[j]
    return new_lis
print(unique_sorted_list([5, 2, 9, 5, 1, 2]))

# Compress a string using the count of repeated characters.
def compress_string_with_count(s):
    compress ={}
    for i in s:
        if i in compress:
            compress[i] +=1
        else:
            compress[i]=1
    new_string = ''
    for i,j in compress.items():
        new_string += f'{i}{str(j)}'
    return new_string
print(compress_string_with_count('maaddiii'))

"""
Topics:
RBAC, Fastapi, SSO: keycloak working

""" 

# find the max char present in the string



"""
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")




design a simple Library Management System in Python.
 
The system should:
 
Allow adding new books with book_id, title, and author.
 
Allow users to borrow a book (if available).
 
Allow users to return a book.
 
Display all available books in the library.

approach:

Library -> books
Users access books
book -> book_id, title, author,boolean: false
user will be assigned with that book
list of books will be sent back for the visiblity




class library():
    def __init__(self,books):
        self.books = books
    def get_books_details(self):
        return self.books
    def add_new_book(self,new_book={}):
        if ['book_id','book_name','Author','Available'] in new_book:
            self.books.append(new_book)
                
    def borrow_book(self,id):
        for i in self.books:
            if i['id'] == id:
                i['Available'] = False
    def return_book(self,id):
        for i in self.books:
            if i['id'] == id:
                i['Available'] = True
class User:
    def __init__(self,users):
        self.user = users
    def borrow_book(self):
        
    
user_id, user_name, book_id,duration
books = [{
    'book_id':1,
    'book_name':'Book1',
    'Author': 'Author1',
    'Avaiable': True
},{
    'book_id':2,
    'book_name':'Book2',
    'Author': 'Author2',
        'Avaiable': True
},
]
l = library(books)
user = [
    {
        
    },
    ]
u = User()



"""
class Book:
    """Represents a single type of book with multiple copies."""

    def __init__(self, book_id: int, title: str, author: str, copies: int = 1):
        """
        Initialize a new Book instance.

        Args:
            book_id (int): Identifier for the book type.
            title (str): Title of the book.
            author (str): Author of the book.
            copies (int): Number of copies available.
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies  # Total copies of this book
        self.borrowed_copies = 0    # How many copies are currently borrowed

    @property
    def available_copies(self) -> int:
        """Return how many copies are available for borrowing."""
        return self.total_copies - self.borrowed_copies

    def __str__(self):
        """Return string representation including available copies."""
        return f"[{self.book_id}] {self.title} by {self.author} - Available: {self.available_copies}/{self.total_copies}"


class Library:
    """A library that can hold multiple copies of the same book."""

    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book_id: int, title: str, author: str, copies: int = 1):
        """
        Add new copies of a book to the library.

        Args:
            book_id (int): Identifier for the book type.
            title (str): Title of the book.
            author (str): Author of the book.
            copies (int): Number of copies to add.
        """
        for book in self.books:
            if book.book_id == book_id:
                # If the book already exists, just increase its total copies
                book.total_copies += copies
                print(f"✅ Added {copies} more copies of '{book.title}'. Total: {book.total_copies}")
                return

        # Otherwise, add as a new book entry
        self.books.append(Book(book_id, title, author, copies))
        print(f"✅ Book '{title}' added with {copies} copies.")

    def display_books(self):
        """Display all books with available copies."""
        if not self.books:
            print("⚠️ No books in the library.")
            return

        print("\n📚 Library Collection:")
        for book in self.books:
            print(f"  {book}")

    def borrow_book(self, book_id: int):
        """Borrow a copy of a book if available."""
        for book in self.books:
            if book.book_id == book_id:
                if book.available_copies > 0:
                    book.borrowed_copies += 1
                    print(f"✅ You borrowed '{book.title}'. Remaining copies: {book.available_copies}")
                else:
                    print(f"⚠️ No copies of '{book.title}' are currently available.")
                return
        print("❌ Book not found!")

    def return_book(self, book_id: int):
        """Return a borrowed copy of a book."""
        for book in self.books:
            if book.book_id == book_id:
                if book.borrowed_copies > 0:
                    book.borrowed_copies -= 1
                    print(f"✅ You returned '{book.title}'. Remaining copies: {book.available_copies}")
                else:
                    print(f"⚠️ No borrowed copies of '{book.title}' to return.")
                return
        print("❌ Book not found!")


# Example usage
# if __name__ == "__main__":
#     library = Library()

#     # Add books (multiple copies allowed)
#     library.add_book(1, "1984", "George Orwell", copies=3)
#     library.add_book(2, "The Great Gatsby", "F. Scott Fitzgerald", copies=2)

#     library.display_books()

#     # Borrow multiple copies
#     library.borrow_book(1)
#     library.borrow_book(1)
#     library.borrow_book(1)
#     library.borrow_book(1)  # Should warn that no copies left

#     library.display_books()

#     # Return a book
#     library.return_book(1)
#     library.display_books()


# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
# # reverse string
# string = "abcdef"
# # print(string[::-1])
# rev_string= ''
# len_s = len(string)
# print('checking',len_s)
# for i in range(len_s):
#     rev_string += string[(len_s-1)-i]
# print(rev_string)

# list of few indexes
# lis = ['eat','ate','ten','net','bet']
# # divide the list as per anagram
# lis2 = []
# dic = {}
# for i in lis:
#     # key check
    
#     for j in dic:
#         for elem in i:
#             for
        
        # if len(i)==len(j):
            
# multiple duplicate value indexes    # 
lis = [1,1,2,3,1,5,6,6,7]
lis2 = set(lis)
dic = {}
for index,val in enumerate(lis):
    if val in lis2:
        if val not in dic:
            dic[val] =[index]
        else:
            dic[val].append(index)
print(dic)


lis = ['eat', 'ate', 'ten', 'net', 'bet']

# Dictionary to group anagrams
anagram_dict = {}

for word in lis:
    # Sort the word to create the key
    key = ''.join(sorted(word))
    anagram_dict.setdefault(key, []).append(word)

# Get the grouped anagrams as a list of lists
lis2 = list(anagram_dict.values())

print(lis2)

    
            

import functools
import logging

# Configure logging (optional)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def exception_handler(default_return=None, raise_exception=False):
    """
    Decorator to handle exceptions in a generic way.

    :param default_return: Value to return if exception occurs (default: None)
    :param raise_exception: If True, re-raise the exception after handling it
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
                if raise_exception:
                    raise
                return default_return
        return wrapper
    return decorator
@exception_handler(default_return="Something went wrong!")
def divide(a, b):
    return a / b

print(divide(10, 2))   # ✅ Output: 5.0
print(divide(10, 0))   # ✅ Logs error, returns "Something went wrong!"

    
