def to_digits_array(a, b):
    digits = []
    while a > 0 or b > 0:
        digits.append((a % 10, b % 10))
        a //= 10
        b //= 10
    return digits

def from_digits_array(digits):
    a, b = 0, 0
    mult = 1
    for ad, bd in digits:
        a += mult * ad
        b += mult * bd
        mult *= 10
    return a, b    

def remove_fours(a, b):
    digits = to_digits_array(a, b)
    for i, (ad, bd) in enumerate(digits):
        j = 1
        while ad == 4 or bd == 4:
            ad, bd = j, ad + bd - j
            j += 1
        digits[i] = (ad, bd)
    return from_digits_array(digits)

t = int(input())
for c in range(t):
    n = int(input())
    a, b = remove_fours(n, 0)
    print('Case #{}: {} {}'.format(c + 1, a, b))
