import sys

count = int(sys.stdin.readline())
position = []

for _ in range(count):
    posX, posY = sys.stdin.readline().split()
    position.append((int(posX), int(posY)))

position.sort(key=lambda x: (x[0], x[1]))

for posX, posY in position:
    print(posX, posY)