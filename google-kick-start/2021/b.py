def read_str():
    return input()

def read_strs():
    return input().split()

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def count_ls(a, b):
    return max(min(a // 2, b) - 1, 0)

def solve(r, c, h):
    count = 0

    for i in range(r):
        for j in range(c):
            n, e, s, w = h[i][j]

            count += count_ls(n, e)
            count += count_ls(e, n)
            count += count_ls(e, s)
            count += count_ls(s, e)
            count += count_ls(s, w)
            count += count_ls(w, s)
            count += count_ls(w, n)
            count += count_ls(n, w)

    return count

tt = read_int()
for cc in range(1, tt + 1):
    r, c = read_ints()

    g = [[False for _ in range(c)] for _ in range(r)]
    h = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]

    for i in range(r):
        row = read_ints()
        for j in range(c):
            x = row[j]
            g[i][j] = x == 1
            h[i][j] = [x, x, x, x]

    for i in range(1, r):
        for j in range(c):
            if g[i][j]:
                h[i][j][0] += h[i-1][j][0]

    for i in range(r):
        for j in range(1, c):
            if g[i][j]:
                h[i][j][1] += h[i][j-1][1]

    for i in reversed(range(r - 1)):
        for j in range(c):
            if g[i][j]:
                h[i][j][2] += h[i+1][j][2]

    for i in range(r):
        for j in reversed(range(c - 1)):
            if g[i][j]:
                h[i][j][3] += h[i][j+1][3]

    ans = solve(r, c, h)
    print(f'Case #{cc}: {ans}')
