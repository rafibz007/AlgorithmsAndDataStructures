from collections import deque

def tanagram( x, y, t ):
    n = len(x)

    positions = [ deque() for _ in range(26) ]

    for i, c in enumerate(y):
        positions[ ord(c)-97 ].append(i)

    for i, c in enumerate(x):
        if not positions[ ord(c)-97 ]: return False

        p = positions[ ord(c)-97 ].popleft()
        if abs(i - p) > t: return False

    return True


x = "kotomysz"
y = "tokmysoz"
print(tanagram(x,y,3))
print(tanagram(x,y,2))
