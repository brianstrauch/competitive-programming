def read_int():
    return int(input())

def solve(x, y, s):
    cost = 0
    c = '?'

    for i in range(len(s)):
        if s[i] == 'C':
            if c == 'J':
                cost += y
            c = 'C'
        elif s[i] == 'J':
            if c == 'C':
                cost += x
            c = 'J'

    return cost

tt = read_int()
for cc in range(1, tt + 1):
    r = input().split()
    x, y, s = int(r[0]), int(r[1]), r[2]
    ans = solve(x, y, s)
    print(f'Case #{cc}: {ans}')
