import math

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def solve(n):
    r, k = 1, 1
    print(r, k)

    k += 1
    h = (-1 + int(math.sqrt(8 * n - 7))) // 2
    for _ in range(h):
        r += 1
        print(r, k)

    k -= 1
    total = h * (h + 1) // 2
    left = n - total - 1
    for _ in range(left):
        print(r, k)
        r += 1

tt = read_int()
for cc in range(1, tt + 1):
    print('Case #{}:'.format(cc))
    n = read_int()
    solve(n)
