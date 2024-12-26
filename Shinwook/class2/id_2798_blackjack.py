import sys

num_of_cards, max_num = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(num_of_cards):
    for j in range(i+1, num_of_cards):
        for k in range(j+1, num_of_cards):
            if cards[i] + cards[j] + cards[k] > max_num:
                continue
            else:
                result = max(result, cards[i] + cards[j] + cards[k])

print(result)






"""
import sys

num_of_cards, max_num = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))

count = 0



    
"""
