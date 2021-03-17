class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        curr.count += 1

        for c in s:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
            curr.count += 1
        curr.is_end = True

    def size(self):
        return self.root.count

    def find(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr

    def contains(self, s):
        node = self.find(s)
        return node and node.is_end

    def count(self, s):
        node = self.find(s)
        return node.count if node else 0

def read_int():
    return int(input())

def solve():
    trie = Trie()

    n = read_int()
    for _ in range(n):
        s = input()
        trie.insert(s[::-1])

    count = 0
    for child in trie.root.children.values():
        c, e = dfs(child)
        count += c
    return count

def dfs(curr):
    count = 0
    extra = 0

    if curr.is_end:
        extra += 1
    for child in curr.children.values():
        c, e = dfs(child)
        count += c
        extra += e

    if extra >= 2:
        return count + 2, extra - 2
    else:
        return count, extra

tt = read_int()
for cc in range(1, tt + 1):
    ans = solve()
    print('Case #{}: {}'.format(cc, ans))
