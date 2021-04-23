import time
import locale
import timeit

# time - UNIX system
print(time.time())

print("\n")
# local
local = locale.setlocale(locale.LC_ALL, ("bulgarian"))
print(local)
print(time.strftime("%A %d %b %Y %H:%M:%S \n %d.%m.%Y"))

print("\n")
# strftime()
dateTime = time.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and time:", dateTime)

print("\n")
# from time import *
from time import *
time1 = time()
def Factoriel(n):
    if n == 0 or n == 1: return 1
    else:
        return n * Factoriel(n - 1)

Factoriel(1000)
time2 = time()
print(time2 - time1)