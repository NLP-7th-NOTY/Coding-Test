N = int(input())
arr = list(input())
result = -1*2**31

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '-':
        return a - b

def dfs(idx, value):
    global result

    if idx == N - 1:
        result = max(result, value)
        return

    if idx+2 < N:
        n_value = calculate(value, arr[idx+1], int(arr[idx+2]))
        dfs(idx+2, n_value)

    if idx+4 < N:
        nn_value = calculate(int(arr[idx+2]), arr[idx+3], int(arr[idx+4]))
        n_value = calculate(value, arr[idx+1], nn_value)
        dfs(idx+4, n_value)


dfs(0, int(arr[0]))
print(result)