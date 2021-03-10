def solve(s):
    ans = ''

    last = 0
    for c in s:
        n = int(c)
        diff = n - last

        if diff > 0:
            ans += diff * '('
        else:
            ans += -diff * ')'
        ans += c

        last = n

    ans += last * ')'
    return ans

tt = int(input())
for cc in range(1, tt + 1):
    s = input()
    ans = solve(s)
    print('Case #{}: {}'.format(cc, ans))
