import re

# For Dates.
# https://stackoverflow.com/questions/15491894/regex-to-validate-date-format-dd-mm-yyyy
# https://www.regular-expressions.info/dates.html

date = input("Enter a date: ")
# dd.mm.yyyy or mm.dd.yyyy
p = re.compile(r"\d{1,2}.\d{1,2}.\d{4}$")

if p.search(date):
    print("Corrnet.")
else:
    print("Incorrect.")

# For emails
text = input("Enter email: ")
pattren = r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.+[a-z]{2,}$"

rg = re.compile(pattren, re.I | re.S)
match1 = rg.search(text)

if match1:
    print("Valid amail.")
else:
    print("Invalid emal.")


# Sub()
def mult(m):
    x = int(m.group(0))
    x *= 2
    return "{0}".format(x)

pattrenV = re.compile(r"[0-9]+")
print(pattrenV.sub(mult, "2, 3, 4, 5, 6, 7"))

print(pattrenV.sub(mult, "2, 3, 4, 5, 6, 7", 3))