import sys
from collections import deque
import copy

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    world_map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    start = deque() 

    for i in range(n):
        for j in range(m):
            if world_map[i][j] == 2 :
                start.append((i, j))
                world_map[i][j] = 0
                original_x = i
                original_y = j
    
    visited = copy.deepcopy(world_map)
    
    first_step = [(original_x, original_y - 1),
                  (original_x, original_y + 1),
                  (original_x - 1, original_y),
                  (original_x + 1, original_y)]
    
    while start:
        x, y = start.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + dx
            new_y = y + dy
            
            if (0 <= new_x < n) and (0 <= new_y < m) and (visited[new_x][new_y] == 1):
                world_map[new_x][new_y] = world_map[x][y] + 1
                visited[new_x][new_y] = 0
                start.append((new_x, new_y))
    
    for i in range(n):
        for j in range(m):
            if (world_map[i][j] == 1) and ((i, j) not in first_step):
                world_map[i][j] = -1 
    
    for row in world_map:
        print(*row)
    
    
if __name__ == "__main__":
    main()

    
    
    
    
                