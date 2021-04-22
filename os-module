import os
import datetime

result = dir(os)
result = os.name


# change directory

os.chdir('C:\\')
os.chdir('../..')


# creating folder

os.mkdir("newdirectory")
os.makedirs("newdirectory/newfolder")
os.rename("newdirectory","newfolder")
os.rmdir("newdirectory")
os.removedirs("newfolder/newfolder")


# listing

result = os.listdir()
result = os.listdir('C:\\')
for file in os.listdir():
    if file.endswith('.py'):
        print(file)

        
# active directory learning

result = os.getcwd()

result = os.stat("_datetime.py")
result = result.st_size/1024
result = datetime.datetime.fromtimestamp(result.st_ctime)  # creation date
result = datetime.datetime.fromtimestamp(result.st_atime)  # last accessed date
result = datetime.datetime.fromtimestamp(result.st_mtime)  # modification date

# os.system("notepad.exe")



# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/python/advanced-modules/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/python/advanced-modules/_os1.py")
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules")
result = os.path.isfile("C:/python/advanced-modules/_os.py")
result = os.path.join("C:\\","trial","trial1")
result = os.path.split("C:\\trial")
result = os.path.splitext("_os.py")
result = result[0]
result = result[1]

print(result)
