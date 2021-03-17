import random
import sys

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

tt, n, m = read_ints()
for cc in range(1, tt + 1):
    possible = set(range(1, m + 1))

    while len(possible) > 1:
        b = random.randint(2, 18)
        blades = [b] * 18
        blades = map(str, blades)
        print(' '.join(blades))
        sys.stdout.flush()

        res = read_ints()
        p = set(range(sum(res), m + 1, b))
        possible = possible.intersection(p)

    print(possible.pop())
    sys.stdout.flush()

    verdict = read_int()
    if verdict == -1:
        sys.exit(1)
