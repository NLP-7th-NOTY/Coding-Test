import sys

hh, mm = map(int,sys.stdin.readline().split())

sk_mm = mm - 45

if sk_mm < 0:
    sk_mm = 60 + sk_mm
    if hh == 0:
        hh = 23
    else:
        hh -= 1

print(hh, sk_mm)