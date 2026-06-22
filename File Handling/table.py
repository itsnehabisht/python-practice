for n in range(2,21):
    with open(f"tables/table_{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n}X{i} = {n*i}\n")