'''Class Book – has 2 attributes – book_id and book_name. Has a constructor.
Class Library – has 3 attributes – library_id, address and a list of book objects. Has 2 functions.
  1.One gets a character as input and returns the count of books starting with that character.
  2.Second function takes a list of book names as input and removes those books from library if present.
input:
3
100
C++ Programming
200
Introduction to SQL
300
Core Java
C
2
Introduction to SQL
Python Programming
Output:
2
C++ Programming
Core Java'''

class Book:
    def _init_(self,id,name):
        self.id=id
        self.name=name
class Library:
    def count_books(arr,c):
        count=0
        for i in arr:
            if i.name.startswith(c):
                count+=1
        return count
    def books_present(arr1,arr2):
        actual=[]
        for i in arr1:
            if i.name not in arr2:
                actual.append(i.name)
        return actual
#main_function
my_list=[]
book_list=[]
n=int(input())
for i in range(n):
    id=int(input())
    name=input()
    my_list.append(Book(id,name))
char=input()
m=int(input())
for i in range(m):
    s=input()
    book_list.append(s)
result1=Library.count_books(my_list,char)
result2=Library.books_present(my_list,book_list)
print(result1)
for i in result2:
    print(i)
