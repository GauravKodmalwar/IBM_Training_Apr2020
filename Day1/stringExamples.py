import sys, os
import builtins
print(sys.path)
sys.path.append("F:\PythonIBMTraining\PythonTraining\Day1")
import session1
print(__name__)
print(session1.__name__) #__main__
varText = "Python string examples"
print(varText.index("string"))
""" String slicing """
""" [start index:end index:switch\step]   """
print(varText[7:13:1])
print(varText[7:13:2])
print(varText[18])
print(varText[10:])
print(varText[:10])
print(varText[::2])
print(varText[::-1])
print(varText[18:7:-2])
print(len(varText))

