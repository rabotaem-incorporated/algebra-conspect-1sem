import os

new_index = ""

for section in sorted(os.listdir("sections")):
    sec_index, *subsections = sorted(os.listdir("sections/" + section))

    with open(f"sections/{section}/!sec.tex") as f:
        sec_index = f.read()
    
    new_sec_index = ""
    for line in sec_index.splitlines(keepends=True):
        if not line.startswith("\import"):
            new_sec_index += line
    
    for ss in subsections:
        new_sec_index += f"\import{{sections/{section}}}{{{ss}}}\n"

    with open(f"sections/{section}/!sec.tex", "w") as f:
        f.write(new_sec_index)

    new_index += f"\import{{sections/{section}}}{{!sec}}\n"


with open("algebra.tex") as f:
    root = f.read()

new_root = ""
skip = False
for line in root.splitlines(keepends=True):
    if line.startswith("% Insert index here!"):
        new_root += "% Insert index here!\n"
        new_root += new_index
        new_root += "% And stop inserting index here!\n"
        skip = True
    elif skip and line.startswith("% And stop inserting index here!"):
        skip = False
    elif skip:
        continue
    else:
        new_root += line

with open("algebra.tex", "w") as f:
    f.write(new_root)
