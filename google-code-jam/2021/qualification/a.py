def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def argmin(L):
    j = 0
    for i in range(1, len(L)):
        if L[i] < L[j]:
            j = i
    return j

def reverse(L, i, j):
    for k in range((j - i + 1) // 2):
        a = i + k
        b = j - k
        L[a], L[b] = L[b], L[a]
    return L

def solve(n, L):
    count = 0
    for i in range(n - 1):
        j = i + argmin(L[i:])
        count += j - i + 1
        L = reverse(L, i, j)
    return count

tt = read_int()
for cc in range(1, tt + 1):
    n = read_int()
    L = read_ints()
    ans = solve(n, L)
    print(f'Case #{cc}: {ans}')
