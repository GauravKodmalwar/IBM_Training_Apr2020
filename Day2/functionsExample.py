def processString(argText, argSpecial="@#%"):
    temp = argText
    for word in argText.split(" "):
        for keyword in argSpecial:
            if keyword in word:
                temp = temp.replace(keyword, "")
    return temp

varText = """
@Python training, going well... dont sleep.
#enjoy your day, see your tomorrow at 8 AM
How is going, learning 100%?
"""
varSpecial = "@#%?"

print(processString(varText, varSpecial))
print(processString(varText))
print(processString(argSpecial=varSpecial, argText=varText))


def addNo(*argNos): # Arbitrary arguments function
    temp = 0
    for no in argNos:
        temp += no
    return temp

#print(addNo(5, 10, 20))
#print(addNo(5, 10, 20, 40, 101, 400, 500))

def processNo(argOperation, *argNos): # Arbitrary arguments function
    temp = 1
    for no in argNos:
        if argOperation == "sum":
            temp += no
        elif argOperation == "multiply":
            temp *= no
    return temp

print(processNo("sum", 5, 10))
print(processNo("multiply", 10, 20, 30))

def greet(*restNames, fname="Default"):
    print("Hello, ", fname)
    for i in restNames:
        print("Hello, ", i)

print(greet("Gaurav", "Hemlatha", "Sasi", fname="Pythoner"))

def greet2(arg1, arg2, arg3, *args4):
    pass