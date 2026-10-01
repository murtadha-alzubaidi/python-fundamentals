class Book:
    def __init__(self,title,pages):
        self.title= title
        self.pages= pages
    def is_long(self):
        return self.pages >= 100
books=[(Book("Python Basics", 120)),(Book("AI Intro",300)),(Book("Git Guide",80)),]
total_pages=0
for book in books:
    print(book.title,book.pages,book.is_long())
    total_pages += book.pages
print("Total Pages:", total_pages)