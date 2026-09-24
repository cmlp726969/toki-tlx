import math

N, M = map(int, input().split())
g = math.gcd(N, M)

N_baru = (N // g) + N
M_baru = (M // g) + M

UbinTambahan = (N_baru * M_baru) - (N * M)
print(UbinTambahan)
