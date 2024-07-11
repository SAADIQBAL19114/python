age = input("Provide me an age: ")
day = input("Provide me day: ")
age_in_int = int(age)
price = 12 if age_in_int > 17 else 8 

if day == "Wednesday":
    price -= 2

print("Ticker price foe you is $", price)


