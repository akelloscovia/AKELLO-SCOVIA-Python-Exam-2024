class Book:
    def _init_(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

 #  b)
class Ebook(Book):
    def _init_(self, title, author, pages, file_size):
        super()._init_(title, author, pages)
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size} MB")
        
# instance of the Ebook class
ebook = Ebook(" Programming", "Emaru", 100, 10)
ebook.display_info()


#(c)
# instance of the Book class
book = Book("Programming", "Emaru", 100)
book.display_info()

