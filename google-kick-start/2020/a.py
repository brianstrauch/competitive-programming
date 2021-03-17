def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def solve(n, b, a):
    count = 0
    for ai in sorted(a):
        if b - ai < 0:
            break
        b -= ai
        count += 1
    return count

tt = read_int()
for cc in range(1, tt + 1):
    n, b = read_ints()
    a = read_ints()

    ans = solve(n, b, a)
    print(f'Case #{cc}: {ans}')
