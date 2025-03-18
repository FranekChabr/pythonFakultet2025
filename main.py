import random

n = 50
k = 30
rule = 30

predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
prerule = ["*" if int(i) else "_" for i in bin(rule)[2:].zfill(8)]
automat = {i: j for i, j in zip(predict, prerule)}

# Poprawione losowanie komórek
cells = "".join(random.choice("_*") for _ in range(n))

for _ in range(k):
    print(cells)
    # Poprawiona obsługa indeksowania
    cells = "".join(
        automat[cells[i - 1] + cells[i] + cells[(i + 1) % n]]
        for i in range(n)
    )


# AUTOMAT 2d NA KARTKOWCE ZA TYDZIEN