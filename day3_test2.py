def conver_price(price_text):
    try:
        price= int(price_text)
    except ValueError:
        return"invalid price"
    if price >= 1000:
        return "expensive"
    elif price >= 300:
        return "normal"
    else :
        return "cheap"
print(conver_price("1500"))
print(conver_price("400"))
print(conver_price("50"))
print(conver_price("ten"))
    