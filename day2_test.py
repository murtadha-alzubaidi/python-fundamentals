city= "baghdad"
temperature= 40
humidity= 35.5
is_raining= True
print("city:", city)
print("temperature:", temperature)
print("humidity:", humidity)
print("is_raining:", is_raining)
print(type(city))
print(type(temperature))
print(type(humidity))
print(type(is_raining))
if temperature >= 45 :
    print("extreme heat")
elif temperature >= 30 :
    print("hot")
elif temperature >= 15 :
    print("mild")
else :
    print("cold")
if is_raining== True :
    print("an umbrella")
else :
    print("no umbrella")

