words = ["donkey", "Twinkle", "sky"]

with open("poem.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("poem.txt", "w") as f:
    f.write(content)