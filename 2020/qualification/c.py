def solve(A):
    n = len(A)

    A = [[s, e, i] for i, [s, e] in enumerate(A)]
    A = sorted(A)

    c = 0
    j = 0

    ans = ['X' for _ in range(n)]
    for s, e, i in A:
        if c <= s:
            c = e
            ans[i] = 'C'
        elif j <= s:
            j = e
            ans[i] = 'J'
        else:
            return 'IMPOSSIBLE'

    return ''.join(ans)

tt = int(input())
for cc in range(1, tt + 1):
    n = int(input())

    A = []
    for _ in range(n):
        a = [int(x) for x in input().split()]
        A.append(a)

    ans = solve(A)
    print('Case #{}: {}'.format(cc, ans))
