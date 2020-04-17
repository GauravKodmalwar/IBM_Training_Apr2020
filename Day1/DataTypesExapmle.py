# List ==> mutable object
# Tuple ==> Immutable object
# Set
# Dictionary
# complex
varList = [10, 20, 40, 50, 23, 45, 64, 23]
print(id(varList))
print(varList)
print(type(varList))
print(varList[0])
print(varList[2])
print(varList[:5:2])
print(len(varList))
print(varList)
print(varList.pop())
print(varList)
varList.append(55)
varList.append(134)
varList.append([134, 242])
print(varList)
varList[2] = "Python"
print(varList)
varList.extend([55, 543])
varList.insert(0, 100000)
print(varList)
print("out of count", varList.count(134))
print("Python training is on Python".count("Python"))
varTuple = (10, 20, 40)
print(varTuple.index(10))
print(varTuple[2])