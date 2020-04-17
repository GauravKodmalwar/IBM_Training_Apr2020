# from packageName.moduleName import function, function2, function3
#from myDBpackage.IOmodule import *
#from myDBpackage.IOmodule import functionFile
import sys
sys.path.append("F:\\PythonIBMTraining2\\Training\\Day3")
import myDBpackage.IOmodule as io
import myDBpackage as pk
import sys, os

print(io.__pi)
print(io.writeConstants())
print(sys.path)
io.functionFile(int(input("Enter a number to write those many lines")), "data")
