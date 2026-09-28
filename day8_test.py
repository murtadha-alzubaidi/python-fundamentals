movies=[{"name":"Inception","rating":9},
        {"name":"Cars","rating":6},
        {"name":"Up","rating":8},
        {"name":"Batman","rating":7},]
def get_lable(rating):
    if rating >= 8:
        return "Good"
    else:
        return "ok"
total=0
lable=0
for movie in movies:
    name =movie["name"]
    rating =movie["rating"]
    get=get_lable(rating)
    total += rating
    print(name,rating,get)
    if get== "Good":
        lable +=1
print("average rating:",total/ len(movies))
print("good movies:",lable)



