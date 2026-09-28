books=[{"title":"Python basics","pages":120},
       {"title":"AI intro","pages":300},
       {"title":"Git guide","pages":80}]
total_pages=0
long_books=0
for book in books:
    title=book["title"]
    pages=book["pages"]
    if pages>=100:
        long_books +=1
    total_pages+=pages
    print(title,pages)
print("total pages:",total_pages)
print("long books:",long_books)