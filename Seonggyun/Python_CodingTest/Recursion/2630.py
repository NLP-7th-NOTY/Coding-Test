"""
import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
raw_paper = [0] * n
raw_paper = np.zeros((n, n), dtype = int)

for i in range(n):
    raw_paper[i] = np.array(list(map(int, sys.stdin.readline().rstrip().split())))

print(raw_paper)
answer_0 = 0
answer_1 = 0

def devide(paper: np.array):
    if np.all(paper == 0):
        global answer_0
        answer_0 += 1
        
    elif np.all(paper == 1):
        global answer_1
        answer_1 += 1
        
    else:
        h, w = paper.shape
        h2, w2 = h // 2, w // 2
        
        top_left = paper[:h2, :w2]
        top_right = paper[:h2, w2:]
        bottom_left = paper[h2:, :w2]
        bottom_right = paper[h2:, w2:]
        
        devide(top_left)
        devide(top_right)
        devide(bottom_left)
        devide(bottom_right)

devide(raw_paper)
print(answer_0)
print(answer_1)
"""
# 위에 처럼 하면 백준에서 안 풀림 ㅋㅋㅋ numpy가 import 안 되더라;;
import sys
import itertools

n = int(sys.stdin.readline().rstrip())
raw_paper = [0] * n

for i in range(n):
    raw_paper[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    
answer_0 = 0
answer_1 = 0

def devide(paper):
    chain = itertools.chain.from_iterable(paper)
    sum_chain = sum(chain)
    len_paper = len(paper)
    target = len_paper ** 2
    
    if sum_chain == 0:
        global answer_0
        answer_0 += 1
    
    elif sum_chain == target:
        global answer_1
        answer_1 += 1
        
    else:
        new_len = len_paper // 2
        
        top_left = [row[:new_len] for row in paper[:new_len]]
        top_right = [row[new_len:] for row in paper[:new_len]]
        bottom_left = [row[:new_len] for row in paper[new_len:]]
        bottom_right = [row[new_len:] for row in paper[new_len:]]
        
        devide(top_left)
        devide(top_right)
        devide(bottom_left)
        devide(bottom_right)

devide(raw_paper)
print(answer_0)
print(answer_1)

    
        
        
    
    
    