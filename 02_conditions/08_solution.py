char = "saadiqbal1234"
password_length = len(char)

if password_length < 6: 
    print("week")
elif password_length <11:
    print("medium")
else :
    print("strong")