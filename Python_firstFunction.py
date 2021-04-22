# Factorial - recursion
def Factoriel(n):
    if n == 0 or n == 1: return 1
    else:
        return n * Factoriel(n - 1)

print(Factoriel(5))

# Pi
import math

def MathPi(num):
    pi = 0.0
    num = int(num)
    for x in range(num):
        pi += math.pow(-1, x) / (2 * x + 1)
    pi *= 4
    return pi

number = float(input("Enter a number \n"))
print(MathPi(number))