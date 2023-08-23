class library:
  def __init__(self,book):
    self.book_list = book
  def show(self):
    print(*self.book_list)
  def lend_book(self,book_name):
    if book_name in self.book_list:
      self.book_list.remove(book_name)
      print('Thankyou, Book issued ')
      return True
    else:
      print("This book is not availabe ")
      return False
    def returnBook(self,book_name):
      self.book_list.append(book_name)
      return True

class customer:
  def __init__(self):
    self.bookList = []
  def add_book(self,book_name):
    self.bookList.append(book_name)
  def show(self):
    print(self.bookList)
  def request_book(self):
    print('Enter the book name to checkout:')
    self.book = input()
    return self.book
  def return_book(self):
    print("Enter the book nsme to check in:")
    self.book = input()
    return self.book
  def lend_book_in_lib(self,book_name):
    if book_name in self.bookList:
      self.bookList.remove(book_name)
      print("you returned the book",'book_name',)
      status=lib_cbe.returnBook(book_name)
      return True
    else:
      print("Returning the wrong book")


lib_cbe = library(['book1','book2','book3','book4','book5','book2'])
preethi = customer()

while True:
  print("------------------")
  print("Select the option below")
  print("1-Show the list of books \n2- Lend a book \n3- Customer borrowed books \n4-Return book \n0-exit")
  option = int(input())
  if option ==1:
    lib_cbe.show()
  elif option == 2:
    requested_book = preethi.request_book()
    status = lib_cbe.lend_book(requested_book)
    if status == True:
      preethi.add_book(requested_book)
  elif option == 3:
    preethi.show()
  elif option ==4:
    returned_book = preethi.return_book()
    status = preethi.lend_book_in_lib(returned_book)

  elif option == 0:
    break

