import random

def dfs(i, j, k):
    if k == r * c:
        return [(i, j)]

    V[i][j] = True

    possible = []
    for ii in range(1, r + 1):
        if i == ii:
            continue
        for jj in range(1, c + 1):
            if j == jj or i + j == ii + jj or i - j == ii - jj:
                continue
            possible.append((ii, jj))
    random.shuffle(possible)

    for ii, jj in possible:
        if not V[ii][jj]:
            path = dfs(ii, jj, k + 1)
            if path:
                path.append((i, j))
                return path

    V[i][j] = False

tt = int(input())
for cc in range(1, tt + 1):
    r, c = [int(x) for x in input().split()]
    V = [[False for _ in range(c + 1)] for _ in range(r + 1)]

    ans = dfs(1, 1, 1)
    if ans:
        print('Case #{}: POSSIBLE'.format(cc))
        for i, j in ans:
            print('{} {}'.format(i, j))
    else:
        print('Case #{}: IMPOSSIBLE'.format(cc))
