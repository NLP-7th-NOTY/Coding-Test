import sys

count = int(sys.stdin.readline())
words = set()

for _ in range(count):
    words.add(sys.stdin.readline().strip())


words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)


