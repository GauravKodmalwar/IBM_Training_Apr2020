# Dynamic keyword argument
def greet(**names):
    print(type(names))
    for key, value in names.items():
        print(key, value)

print(greet(firstname="Gaurav", langauge="Python"))
temp = {'firstname':"Gaurav", 'langauge':"Python"}
print(greet(**temp))

def greet(word, **names):
    print(type(names))
    for key, value in names.items():
        print(word, key, value)

print(greet(word="Hello", firstname="Gaurav", langauge="Python"))

def greet(word, *args, **names):
    print(word)
    print([i for i in args])
    print([key + ":" + value for key, value in names.items()])

print(greet("hello"))
print(greet("hello", 37, "15-Oct"))
print(greet("hello", 37, "15-Oct", firstname="Gaurav", langauge="Python"))
