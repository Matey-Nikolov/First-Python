# Ще изведе true, защото се отнасят към един и същи обекти.
a = b = [5, 4, 3]
print(a is b) 
print()

# Ще изведе false, защото се отнасят към различни обекти.
a = [5, 4, 3]
b = [5, 4, 3]
print(a is b) 
print()

# Преобразуване.
x = float (input("Enter x = \n"))
y = float (input("Enter y = \n"))
print(x +y)
print()

# Оператори 
print(2 + 2) # Отговора е цяло число
print(2 - 2.0) # реално число
print(100 / 5) # Явява се реално число
print(100 // 33) # Закръгля надолу
print(100 % 33) # Остатък от делението
print()

# First Program - If else
print("""Select your bwouser:
1 - Google Chrome
2 - Firefox
3 - Opera""")

browser = int(input(""))
if browser == 1:
    print("Google Chrome")
elif browser == 2:
    print("Firefox")
elif browser == 3:
        print("Opera")
else:
    print("Incorrect input")

print()

# Second Program - Sorted Dictionary
dict = {'a' : 1, 'b': 2}
for key in sorted(dict.keys()):
    print(key, "=>", dict[key])