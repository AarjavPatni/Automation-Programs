import os

dirList = []
for i in os.walk(r"C:\Users\Aarjav\Documents\Second Brain\Goals"):
    for k in i[2]:
        dirList.append(f"{i[0]}\{k}") if k.endswith(".md") else None

write = False

if input('Are you sure? (y/N) ').lower() == "y":
    for i in dirList:
        with open(i, "r", encoding="utf8") as f:
            try:
                content = f.read()
                write = True
            except:
                write = False

        content = content.replace("- [x] Today", "- [ ] Today")

        if write:
            with open(i, "w", encoding="utf8") as f:
                f.write(content)

print('Done! New day tomorrow!')
