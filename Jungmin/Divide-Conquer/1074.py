N, r, c = map(int, input().split(' '))
idx = 0

while N != 0:
    mid_ = ((2**N) // 2) - 1
    jmp_cnt = int(((2**N)**2) / 4)

    if c <= mid_ and r <= mid_:
        idx += 0

    elif c > mid_ >= r:
        idx += jmp_cnt
        c -= (mid_ + 1)

    elif c <= mid_ < r:
        idx += jmp_cnt * 2
        r -= (mid_ + 1)

    elif c > mid_ and r > mid_:
        idx += jmp_cnt * 3
        c -= (mid_ + 1)
        r -= (mid_ + 1)

    N -= 1

print(idx)