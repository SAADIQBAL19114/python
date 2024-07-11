age = input("Provide me an age: ")

age_in_int = int(age)

if age_in_int < 13:
    print("child")
elif age_in_int < 20:
    print("teenager")
elif age_in_int < 60:
    print("adult")
else:
    print("senior")

