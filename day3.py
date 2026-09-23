def greet():
    print("hello murtadha")
greet()
def add(a,b):
    return a + b
result= add(3,4)
print(result)
def check_age(age):
    if age >= 18:
        return "adult"
    else:
        return "minor"
print(check_age(20))
print(check_age(15))

try:
    number= int("abc")
    print(number)
except ValueError:
    print("not a number")
def safe_divide(c,d):
    try:
        return c/d
    except ZeroDivisionError:
        return "cannot divide by zero"
print(safe_divide(10,2))
print(safe_divide(10,0))
