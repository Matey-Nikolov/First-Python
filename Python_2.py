age = input("Enter you age: ")

if age.isdigit() == True:
    print("Ok")
else:
    print("Try again")
    age = input("Enter you age: ")
    if age.isdigit() == True:
        print("Ok")
    else:
        print("Error")



