import sys

num = int(input())
word_list = []
for _ in range(num):
    temp = sys.stdin.readline().strip()
    word_list.append(temp)

word_list = list(set(word_list))
    
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)