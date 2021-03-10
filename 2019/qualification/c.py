def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())
for c in range(t):
    n, l = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    # Find first prime
    i = 0
    while C[i] == C[i + 1]:
        i += 1
    prime = C[i] // gcd(C[i], C[i + 1])

    while i > 0:
        prime = C[i] // prime
        i -= 1

    P = [prime]
    for i in range(l):
        prime = C[i] // prime
        P.append(prime)

    A = sorted(list(set(P)))
    for i in range(l + 1):
        P[i] = chr(ord('A') + A.index(P[i]))
    p = ''.join(P)

    print('Case #{}: {}'.format(c + 1, p))
