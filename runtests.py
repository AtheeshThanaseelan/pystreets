import os

programs = []

for file in os.listdir("test/"):
    if(file.find(".py") != -1):
        if(file != "__init__.py"):
            programs.append(file)

print("Select Test")
print("0) Exit")
idx = 0
for program in programs:
    idx += 1
    print(str(idx)+") "+program)

choice = input()
if(choice == "0"):
    exit()

    
choice = programs[int(choice)-1]
choice = "test." + choice
__import__(choice)