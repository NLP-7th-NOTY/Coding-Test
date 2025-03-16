import sys


def dfs():
    


def main():
    V = int(input())

    graph = [[] for _ in range(V + 1)]

    for _ in range(V):
        temps = list(map(int, sys.stdin.readline().rstrip().split()))
        weight = 0
        node = 0
        root = temps[0]

        for index, temp in enumerate(temps[1:]):
            if temp < 0:
                continue

            if (index % 2) == 0:
                weight = temp

            else:
                node = temp

            if weight and node:
                graph[root].append((node, weight))
                weight = 0
                node = 0

    
    
    print(graph)


             




if __name__ == "__main__":
    main()