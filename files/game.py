import random

def game():
    return random.randint(1,100)
newscore = game()
with open("hiscore.txt", "r") as f:
    content = f.read().strip()

    if content == "":
        score = 0
    else:
        score = int(content)

if newscore>score:
    with open("hiscore.txt", "w")as f:
        f.write(str(newscore))
print(newscore)