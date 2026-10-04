class Student:
    def __init__(self,name,score):
        self.name =name
        self.score =score
    def grade(self):
        if self.score >=90:
            return "Excellent"
        elif self.score >=50:
            return "Pass"
        else:
            return "Fail"
    def passed(self):
        return self.score >=50
def read_number(text):
    try:
        return int(text)
    except:
        return -1
students =[Student("ali",95),Student("sara",40),]
count =read_number(input("How many students to add?"))
if count ==-1:
    print("Invaild number")
else:
    for i in range(count):
        name =input("Name:")
        score =read_number(input("Score:"))
        if score ==-1:
            print("Invaild score, skipped",name)
        else:
            students.append(Student(name,score))
total =0
passed_count =0
for student in students:
    print(student.name,student.score,student.grade())
    total += student.score
    if student.passed():
        passed_count +=1
print("Average:",total /len(students))
print("Passed",passed_count)