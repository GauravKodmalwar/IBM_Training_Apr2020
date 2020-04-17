def functionFile(num, filePath):
    with open(filePath + "//sdfsdf/" + "funF_" + str(num), "a+") as file:
        for i in range(num):
           file.write("Content readed successfully, closing file\n")
        file.close()

try:
    pass
    if "10".isdigit() == False:
        raise Exception("Invalid number")
    #15 / 0
    #file = open("Data/Dtata/adta/file.txt", "a+")
    file = open("Data/asdf/asdfasdftextFile7", "a+")
except ZeroDivisionError as e:
    print("Sorry, you are trying to devide by 0 which is mathematically incorrect.", e.__str__())
    print("Closing database connection")
    print("Job failed")
except FileNotFoundError as e:
    print("Couldn't find folder structure. ", e.__str__())
except Exception as e:
    print(e.__str__())
else:
    print("Things are successfully, great job")
    file.close()
finally:
    print("Coming out of reusable function")



#functionFile(int(input(
 #   "Enter a number to write those many lines")), "data")

# Exception handling. Correcting error or you can give valid error message to consumer.

