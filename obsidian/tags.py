import os

# Use os.scandir to find md files in /home/aarjav/Documents/Second Brain/

dirs = os.walk("/home/aarjav/Documents/Second Brain/")

tag = input("Which tag to replace? ")
target = input("What to replace with? ")

for dir in dirs:
    for file in dir[2]:
        if ("workspace" not in file) and (not file.startswith(".")) and ("tags.py" not in file):
            if dir[0][-1] != "/":
                path = dir[0] + "/" + file
            else:
                path = dir[0] + file

            with open(path, "r") as f:
                content = f.read()
            
            content = content.replace(f"#{tag}", f"#{target}")
            with open(path, "w") as f:
                f.write(content)