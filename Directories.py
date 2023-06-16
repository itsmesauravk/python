from pathlib import Path

#type1
path = Path("modules_import")
print(path.exists())  #if we use .mkdir instead of .exists it will make new directory

path = Path("Pipy_pip")
print(path.mkdir())  #this makes directory 
print(path.rmdir())  #this remove directory
print(path.exists()) #this check weather directory exists or not

#type2

path = Path()
print(path.glob('*.py'))  #this will print all the files with end .py
# the above is advance so in this level we can do below
for file in path.glob('*.py'): #glob is used to search files if * used all files will display 
    print(file) #this will print all the .py files present in he directory

