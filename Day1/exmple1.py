temp = int(input("Enter number"))

temp2, temp3 = [], []
for i in range(temp):
    if i == 0:
        None
    elif i % 2 == 0:
        temp2.append(i)
    else:
        temp3.append(i)

print(temp2)
print(temp3)