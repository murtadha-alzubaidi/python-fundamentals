def get_grade(score):
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "fail"
def read_number(text):
    try:
        return int(text)
    except ValueError:
        return -1
students= [{"name":"ali","score":95},
           {"name": "sara","score":72},]
count= read_number(input("how many students to add"))
if count ==-1:
    print("invalid number, no students added")
else:
    for i in range(count):
        name= input("name:")
        score= read_number(input("score:"))
        if score ==-1:
            print("invaild score , skipped", name)
        else:
            students.append({"name": name,"score": score})
total=0
for student in students:
    grade=get_grade(student["score"])
    print(student["name"],student["score"],grade)
    total+= student["score"]
print ("avarage:",total/len (students))