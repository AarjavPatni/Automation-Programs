import os


def svg_encode(svg):
    # Ref: https:\\\\bl.ocks.org\\jennyknuth\\222825e315d45a738ed9d6e04c7a88d0
    # Encode an SVG string so it can be embedded into a data URL.
    enc_chars = '"%#{}<>'  # Encode these to %hex
    enc_chars_maybe = "&|[]^`;?:@="  # Add to enc_chars on exception
    svg_enc = ""
    # Translate character by character
    for c in str(svg):
        if c in enc_chars:
            if c == '"':
                svg_enc += "'"
            else:
                svg_enc += "%" + format(ord(c), "x")
        else:
            svg_enc += c
    return " ".join(svg_enc.split())  # Compact whitespace


dirList = []
hidden = [".trash", ".stfolder", ".stversions", ".obsidian"]

for i in os.walk("C:\\Users\\Aarjav\\Documents\\Second Brain\\"):
    dirList.append(
        i[0].replace("C:\\Users\\Aarjav\\Documents\\Second Brain\\", "").replace("\\", "/")
    ) if not bool([ele for ele in hidden if (ele in i[0])]) else None

for count, k in enumerate(dirList):
    print(f"{count}. {k}") if count > 0 else None

folder = dirList[int(input("\nEnter the folder no.: "))]
svg = input("\nEnter svg: ")
svg = (("data:image/svg+xml," + svg_encode(svg)).replace(r"%3e", r"%3E")).replace(
    r"%3c", r"%3C"
)

code = f""".theme-light div.nav-folder-title[data-path="{folder}"] div.nav-folder-title-content::before {{
	content: url("{svg}")
}}

.theme-dark div.nav-folder-title[data-path="{folder}"] div.nav-folder-title-content::before {{
	content: url("{svg.replace("svg+xml,%3Csvg xmlns", "svg+xml,%3Csvg fill='white' xmlns")}")
}}"""

with open("C:\\Users\\Aarjav\\Documents\\Second Brain\\.obsidian\\snippets\\icons.css", "a") as f:
    f.write("\n" + code + "\n")

print("Done!")
