def trace(arr):
    return sum(arr[i][i] for i in range(len(arr)))

def repeating_rows(arr):
    r = 0
    for i in range(len(arr)):
        seen = set()
        for j in range(len(arr)):
            if arr[i][j] in seen:
                r += 1
                break
            else:
                seen.add(arr[i][j])
    return r

def repeating_cols(arr):
    c = 0
    for j in range(len(arr)):
        seen = set()
        for i in range(len(arr)):
            if arr[i][j] in seen:
                c += 1
                break
            else:
                seen.add(arr[i][j])
    return c

tt = int(input())

for cc in range(1, tt + 1):
    n = int(input())

    M = []
    for i in range(n):
        M.append([int(x) for x in input().split()])

    k = trace(M)
    r = repeating_rows(M)
    c = repeating_cols(M)

    print('Case #{}: {} {} {}'.format(cc, k, r, c))

