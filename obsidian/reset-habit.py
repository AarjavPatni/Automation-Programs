import os
import re

args = os.sys.argv

dirList = []
for i in os.walk(r"C:\Users\Aarjav\Documents\Second Brain\Goals"):
    for k in i[2]:
        dirList.append(f"{i[0]}\{k}") if k.endswith(".md") else None

write = False

for i in dirList:
    with open(i, "r", encoding="utf8") as f:
        try:
            content = f.read()
            write = True
        except Exception:
            write = False

    content = content.replace("- [x] Today", "- [ ] Today")

    if write:
        with open(i, "w", encoding="utf8") as f:
            f.write(content)

print('Done! New day tomorrow!')

if len(args) > 1:
    if args[1].lower() == 'def':
        for k in dirList:
            with open(k, "r", encoding="utf8") as f:
                try:
                    content = f.read()
                    write = True
                except Exception:
                    write = False

            content = content.replace(
                "- [x] Today", "- [ ] Today"
            ).replace(
                "- [x] 1 Day", "- [ ] 1 Day"
            ).replace(
                "- [x] 3 Days", "- [ ] 3 Days"
            ).replace(
                "- [x] 7 Days", "- [ ] 7 Days"
            ).replace(
                "- [x] 15 Days", "- [ ] 15 Days"
            ).replace(
                "- [x] 30 Days", "- [ ] 30 Days"
            )

            # Replace all lines that start with 'day-one: ' to 'day-one: today'
            content = re.sub(r'^day-one:.*', 'day-one: today',
                            content, flags=re.MULTILINE)
            try:
                # Replace all lines that start with 'skips-dates:' to 'skips-dates: ' until '---' is found
                content = re.sub('skips-dates:(?s:.)*?(---)',
                                'skips-dates:\n---', content, flags=re.MULTILINE)
            except Exception as e:
                print(e, k)

            if write:
                with open(k, "w", encoding="utf8") as f:
                    f.write(content)

        print('Restored Defaults!')
