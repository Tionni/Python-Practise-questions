from pathlib import Path
path = Path("pi.txt")
try:
    content = path.read_text()
except FileNotFoundError:
    print(f"sorry, the file {path} does not exist.")
else:
    lines = content.splitlines()
    for line in lines:
        print(line)
    #count the approximate number of words in the file
    words = content.split()
    num_words = len(words)
    print(f"{path} has {num_words} words")