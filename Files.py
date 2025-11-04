# file = open("firstFile.txt", "r")
# count = 0
# #file.write("This is my first file writing")
# for line in file:
#     line = line.strip()
#     print(f"{line}")
#     count += 1
# print(f"{count} lines in file")
# file.close()




def readfile(filename):
    filename = open(filename, "r")
    for line in filename:
        line = line.strip()
        print(line.upper())
    filename.close()

def writefile(filename):
    file = open(filename, "w")
    file.write("Steven")
    file.write("\nJenna")
    file.write("\nJim")
    file.write("\nTim")
    file.write("\nBen")
    file.close()


def appendfile(filename, names):
    file = open(filename, "a")
    for name in names:
        file.write(f"\n{name}")
    file.close()

filePath = "D:\\Users\\acct6\\Downloads\\Students.txt"
try:
    writefile(filePath)
    readfile(filePath)
    print("---------")
    appendfile(filePath, ["Andy", "Nathalie"])
    readfile(filePath)
except FileNotFoundError:
    print(f"File {filePath} not found. Please try again.")
except PermissionError:
    print(f"File {filePath} does not have permission to write/read.")
except Exception as e:
    print(f"Something went wrong.")