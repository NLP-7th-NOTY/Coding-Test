arr = []
T = int(input())
for i in range(T):
    arr.append(int(input()))

f = [[0 for _ in range(7)] for _ in range(100)]
f[1][0] = 1
f[2][0] = 1
f[2][1] = 1
f[3][0] = 1
f[3][2] = 1
f[3][3] = 1
f[4] = [1,1,0,1,1,0,0]
f[5] = [1,0,0,2,1,1,0]
f[6] = [1,1,1,1,1,0,1]

for i in range(7, 100):
    f[i][0] = 1
    f[i][1] = 1 if i % 2 == 0 else 0
    f[i][2] = 1 if i % 3 == 0 else 0
    f[i][3] = f[i-3][0] + f[i-3][1] + f[i-3][3] if i >= 3 else 0
    f[i][4] = f[i-4][0] + f[i-4][2] + f[i-4][4] if i >= 4 else 0
    f[i][5] = f[i-5][1] + f[i-5][2] + f[i-5][5] if i >= 5 else 0
    f[i][6] = sum(f[i-6]) if i >= 6 else 0

for elem in arr:
    print(sum(f[elem]))

res = []
for elem in f[1:]:
    res.append(sum(elem))

f = [1,2,3]

for i in range(4, 10001):
    f.append(f[i-4]+(i//2)+1)

res2 = []
for elem in f:
    res2.append(elem)

print(res)
print(res2)