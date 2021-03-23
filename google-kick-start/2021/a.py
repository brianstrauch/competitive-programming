def read_str():
    return input()

def read_strs():
    return input().split()

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def solve(n, k, s):
    goodness = 0
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            goodness += 1
    return abs(k - goodness)

tt = read_int()
for cc in range(1, tt + 1):
    n, k = read_ints()
    s = read_str()

    ans = solve(n, k, s)
    print(f'Case #{cc}: {ans}')
