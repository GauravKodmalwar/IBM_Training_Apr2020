# string ==> immutable
#List ==> mutable
#Tuple==> immutable
#Set  ==>  mutable, stores unique values and unordered no indexing
#Dictionary ==> mutable {key:value, key2:value}

varSet = {10, 20, 30, 20, 10}
varSet2 = {80, 78, 30, 98, 10}
print(varSet.intersection(varSet2))
print(varSet.union(varSet2))
print(varSet2.difference(varSet))
print(varSet.symmetric_difference(varSet2))

varDict = {5:"Python Day 1", 8:"Python Day 2", 3:"Python Day 3"}
print(varDict.get(1))
print(varDict.keys())
print(varDict.values())
varDict[5] = "Python Day 1 Completed"
print(varDict)
for i in varDict.keys():
    varDict[i] = varDict.get(i) + " Planned"