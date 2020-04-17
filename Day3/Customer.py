class Cars():
    def __init__(self, varCarType, varFuelType, varBrandName):
        self.vCarType = varCarType
        self.vBrandName = varBrandName
        self.__vFuelType = varFuelType

    def get(self):
        return self.__vFuelType

    def update(self, varFuelType):
        self.__vFuelType = varFuelType

class RetailCar(Cars):
    def __init__(self, varCarType, varFuelType, varBrandName, varMileage, varNoWheel):
        super().__init__(varCarType, varFuelType, varBrandName)
        self.vMileage = varMileage
        self.vNoWheel = varNoWheel

    def update(self, varFuelType, varMileage):
        #super().update(varFuelType)
        self.__vFuelType = varFuelType
        self.vMileage = varMileage

    def get(self):
        return self.vMileage, self.vCarType

if __name__ == "__main__":
    obj = Cars("Commercial", "Diesel", "Tata") # creating object of a class
    print(obj.get())
    obj.update("CNG")
    print(obj.vCarType)
    print(obj.vBrandName)
    retail = RetailCar("Retail", "Petrol", "Tata", 18, 4)
    print(retail.vMileage)
    print(retail.vCarType)
    print(retail.get())
    retail.update("CNG", 100)
    print(retail.vMileage)
    print(retail.get())
elif __name__ == "Customer":
    print("Good luck, you have improted my package")