def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def reverse(L, i, j):
    for k in range((j - i + 1) // 2):
        a = i + k
        b = j - k
        L[a], L[b] = L[b], L[a]
    return L

def solve(n, c):
    if c < n - 1 or c > sum(range(2, n + 1)):
        return 'IMPOSSIBLE'

    t = c - (n - 1)
    s = []
    for i in reversed(range(n)):
        m = min(t, i)
        s.append(m + 1)
        t -= m

    L = list(range(1, n + 1))
    for i in reversed(range(n - 1)):
        L = reverse(L, i, i + s[i] - 1)

    return ' '.join([str(x) for x in L])

tt = read_int()
for cc in range(1, tt + 1):
    n, c = read_ints()
    ans = solve(n, c)
    print(f'Case #{cc}: {ans}')
