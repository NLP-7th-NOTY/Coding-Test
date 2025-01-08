import sys

N = int(input())
S, M, L, XL, XXL, XXXL = map(int, sys.stdin.readline().rstrip().split())
T, P = map(int, sys.stdin.readline().rstrip().split())

Ts = 0
Ps = 0

if S:
    S_q, S_r = divmod(S, T)
    if S_r:
        Ts += S_q + 1
    if not S_r:
        Ts += S_q

if M:
    M_q, M_r = divmod(M, T)
    if M_r:
        Ts += M_q + 1
    if not M_r:
        Ts += M_q

if L:
    L_q, L_r = divmod(L, T)
    if L_r:
        Ts += L_q + 1
    if not L_r:
        Ts += L_q

if XL:
    XL_q, XL_r = divmod(XL, T)
    if XL_r:
        Ts += XL_q + 1
    if not XL_r:
        Ts += XL_q
        
if XXL:
    XXL_q, XXL_r = divmod(XXL, T)
    if XXL_r:
        Ts += XXL_q + 1
    if not XXL_r:
        Ts += XXL_q
        
if XXXL:
    XXXL_q, XXXL_r = divmod(XXXL, T)
    if XXXL_r:
        Ts += XXXL_q + 1
    if not XXXL_r:
        Ts += XXXL_q
        
print(Ts)

if N >= P:
    P_q, P_r = divmod(N, P)
    print(P_q, P_r)

else:
    print(0, N)
    
    