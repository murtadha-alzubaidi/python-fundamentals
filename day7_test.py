def get_category(amount):
    if amount >= 100:
        return "big"
    elif amount >= 20:
        return "medium"
    else:
        return "small"
def read_amount(text):
        try:
            return int(text)
        except ValueError:
            return -1
expenses= [{"item":"food","amount":25},
            {"item":"phon","amount":150},]
count= read_amount(input("how many expenses to add?"))
if count==-1:
     print("invalid number")
else:
     for i in range(count):
          item=input("item:")
          amount=read_amount(input("amount"))
          if amount==-1:
               print("invaild amount,skipped")
          else:
               expenses.append({"item":item,"amount":amount})
total=0
big_count=0
for expense in expenses:
     category=get_category(expense["amount"])
     print(expense["item"],expense["amount"],category)
     total += expense["amount"]
     if category=="big":
          big_count+=1
print("total:",total)
print("big expenses:",big_count)