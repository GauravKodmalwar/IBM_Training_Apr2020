# lambda function ==> dynamically created, annomyous function
# single statement

calSquare = lambda i: i ** 2
print(calSquare(5))

sayGreet = lambda name: "Hello, " + name
print(sayGreet("Python"))
print(sayGreet(""))

# Mapper, Filter, Reduce
print(list(map(calSquare, [10, 20, 30, 40])))
print([calSquare(i) for i in [10, 20, 30, 40]])
print(list(map(lambda i: i ** 2, [10, 20, 30, 40])))

# Filter ==> apply condition to filter input data
print(list(filter(lambda i: i%20 == 0, [10, 20, 30, 40])))

def f1(i, j):
    return i * j

from functools import reduce
print(reduce(f1, [10, 20, 30, 40]))

# reducer
# return maximum number, write a function. [10, 20, 3300, 10]
#filter
# return output if it contains special character ["Pyhon!", "Py"]
# Lunch break till 1.00 PM


varText = """
@Python training, going well... dont sleep.
#enjoy your day, see your tomorrow at 8 AM
How is going, learning 100%?
"""
varSpecial = "@#%?"

def processString(argText, argSpecial="@#%"):
    temp = argText
    for keyword in argSpecial:
        if keyword in argText:
            return True
    return False

print(varText.split(" "))
print(list(filter(processString, varText.replace("\n", ".").replace(".", " ").split(" "))))

