class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
    def level(self):
        if self.salary >= 2000:
            return "Senior"
        elif self.salary >= 1000:
            return "Mid"
        else:
            return "Junior"
    def is_high_paid(self):
        return self.salary >= 1500
def read_number(text):
    try:
        return int(text)
    except ValueError:
        return -1
employees=[Employee("Ahmed",2400),Employee("Zainab",900),]
count= read_number(input("How many Employees to add?"))
if count==-1:
    print("Invaild number,skipped")
else:
    for i in range(count):
        name= input("Name:")
        salary= read_number(input("Salary:"))
        if salary==-1:
            print("Invaild salary,skipped",name)
        else:
            employees.append(Employee(name,salary))
total=0
meow=0
for employee in employees:
    print(employee.name,employee.salary,employee.level())
    total += employee.salary
    if employee.is_high_paid():
        meow +=1
print("Total salaries:",total)
print("Average salary:",total /len(employees))
print("High paid:",meow)