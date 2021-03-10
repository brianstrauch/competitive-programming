t = int(input())
for c in range(t):
    n = int(input())
    p = input()
    p = p.replace('S', 'T').replace('E', 'S').replace('T', 'E')
    print('Case #{}: {}'.format(c + 1, p))
