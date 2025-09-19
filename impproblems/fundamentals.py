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