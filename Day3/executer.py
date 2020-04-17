from Customer import *
import sys, os

if __name__ == "__main__":
    obj = Cars("Commercial", "Diesel", "Tata") # creating object of a class
    print(obj.get())
    obj.update("CNG")