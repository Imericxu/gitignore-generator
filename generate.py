import requests
import json
import sys

names = sys.argv[1:]

with open('types.json') as f:
    templates = json.load(f)
f = open('generated.gitignore', 'w')

for name in names:
    # `header` is a "flowerbox" comment to separate the different types
    header = 30 * "#" + "\n"
    header += "# " + name + (27 - len(name)) * " " + "#\n"
    header += 30 * "#" + "\n\n"
    f.write(header)
    # Appends the contents of the .gitignore template
    r = requests.get(
        "https://raw.githubusercontent.com/github/gitignore/master/" + templates[name])
    f.write(r.text)
    f.write('\n')
