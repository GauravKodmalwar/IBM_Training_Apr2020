def functionFile(num, filePath):
    with open(filePath + "//sdfsdf/" + "funF_" + str(num), "a+") as file:
        for i in range(num):
           file.write("Content readed successfully, closing file\n")
        file.close()

# default everything is public. Access modifier.
__pi = 22/7 # private

def writeConstants():
    return __pi