def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def get_interest(arr):
    interest = 0
    for row in arr:
        interest += sum(row)
    return interest

def get_n(i, j, r, c, arr):
    for ii in range(i - 1, -1, -1):
        if arr[ii][j] > 0:
            return arr[ii][j]
    return 0

def get_s(i, j, r, c, arr):
    for ii in range(i + 1, r):
        if arr[ii][j] > 0:
            return arr[ii][j]
    return 0

def get_e(i, j, r, c, arr):
    for jj in range(j + 1, c):
        if arr[i][jj] > 0:
            return arr[i][jj]
    return 0

def get_w(i, j, r, c, arr):
    for jj in range(j - 1, -1, -1):
        if arr[i][jj] > 0:
            return arr[i][jj]
    return 0

def run_round(r, c, arr):
    res = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            count = 0
            n = get_n(i, j, r, c, arr)
            if n > 0:
                count += 1
            s = get_s(i, j, r, c, arr)
            if s > 0:
                count += 1
            e = get_e(i, j, r, c, arr)
            if e > 0:
                count += 1
            w = get_w(i, j, r, c, arr)
            if w > 0:
                count += 1

            res[i][j] = arr[i][j]
            if count > 0:
                avg = (n + s + e + w) / count
                if arr[i][j] < avg:
                    res[i][j] = 0

    return res

def solve(r, c, arr):
    total_interest = 0
    has_changed = True
    while has_changed:
        total_interest += get_interest(arr)
        next = run_round(r, c, arr)
        has_changed = (arr != next)
        arr = next

    return total_interest

tt = read_int()
for cc in range(1, tt + 1):
    r, c = read_ints()
    arr = [[] for _ in range(r)]
    for i in range(r):
        arr[i] = read_ints()
    ans = solve(r, c, arr)
    print('Case #{}: {}'.format(cc, ans))
