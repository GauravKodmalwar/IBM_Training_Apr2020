varList = [10, 30, 40, 50, 20]
# single statement in List Comprehension
temp = [i*10 for i in varList]
print(temp)
print([i for i in range(20) if i % 2 == 0])
print([i for i in range(20) if i % 2 != 0])

print([i if i % 2 == 0 else i + 1 for i in range(20)])

#replacee these special chars with SPECIAL
varText = """
@Python training, going well... dont sleep.
#enjoy your day, see your tomorrow at 8 AM
How is going, learning 100%?
"""
varSpecial = ['@', '#', '%']

temp = varText
for word in varText.split(" "):
    for keyword in varSpecial:
        if keyword in word:
            temp = temp.replace(keyword, "")
print(temp)


"""
# For loop
print(30 in varList)
print("Python Training Day 4".split(" "))
for i in "Python Training Day 4":
    print(i)

i = 0
while(i < 5):
    if i % 2 == 0:
        print(i)
    i += 1

for i in range(5):
    if i % 2 == 0:
        print(i)
"""