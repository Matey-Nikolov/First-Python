import random

# List
list1 = [1, 2, 3, 4]
print(list1[1])

list2 = list("Hello")
print(list2)

list3 = [1, 2, 3, 4, 5, 6]
list3.insert(0, 0)
print(list3)

# Reverse list
n = int(input("Enter a number: "))
a = 0
newList = []
while a < n:
    num = int(input("Enter a numer: "))
    
    newList.append(num)

    a+= 1

reversedList = newList[::-1]
print("Reverse: ")
print(reversedList)

# Accidental displacement
randomList = [1, 2, 3, 4, 5, 6]
random.shuffle(randomList)
print(randomList)

# Char list to string
charList = ['H', 'e', 'l', 'l', 'o']
stringL = "".join(charList)
print(stringL)