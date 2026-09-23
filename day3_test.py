def sara(name):
    print("wellcome",name)
sara("murtadha")
sara("ali")
def grade(score_text):
    try:
       score = int(score_text)
    except ValueError:
       return "invalid input"
    if score >= 90:
     return "excellent"
    elif score >= 50:
        return "pass"
    else :
       return "fail"
print(grade("95"))
print(grade("40"))
print(grade("abc"))