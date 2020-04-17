varList = [10, 20, 40, 60]
varTemp = varList.copy()

varTemp[2] = 10030000
print(varList)
print(id(varList))
print(id(varTemp))