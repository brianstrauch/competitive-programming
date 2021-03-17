def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def is_prefix(s, prefix):
    n = len(prefix)
    if n == 0:
        return True
    return s[:n] == prefix

def is_suffix(s, suffix):
    n = len(suffix)
    if n == 0:
        return True
    return s[-n:] == suffix

def solve():
    n = read_int()

    longest_l = ''
    longest_r = ''
    inner = ''
    for _ in range(n):
        s = input()

        first_idx = s.index('*')
        last_idx = len(s) - 1 - s[::-1].index('*')
        inner += s[first_idx+1:last_idx].replace('*', '')
        l = s[:first_idx]
        r = s[last_idx+1:]

        if len(l) > len(longest_l):
            if is_prefix(l, longest_l):
                longest_l = l
            else:
                longest_l = '*'
        else:
            if not is_prefix(longest_l, l):
                longest_l = '*'

        if len(r) > len(longest_r):
            if is_suffix(r, longest_r):
                longest_r = r
            else:
                longest_r = '*'
        else:
            if not is_suffix(longest_r, r):
                longest_r = '*'

    if longest_l == '*' or longest_r == '*':
        return '*'

    return longest_l + inner + longest_r

tt = read_int()
for cc in range(1, tt + 1):
    ans = solve()
    print('Case #{}: {}'.format(cc, ans))
