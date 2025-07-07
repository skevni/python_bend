"""
10
8 2 4 7 8 5 5 8 6 9
13
9 8 1 1 1 5 10 8 2 7 4 3 15

8 8  8  9  7 6 5 5 4 2  
9 10 15    8 7 8   5 3
"""


def t1():
    a = sorted([int(x) for x in '8 5 5 8 6 9 8 2 4 7'.split()], reverse=True)
    b = sorted([int(x) for x in '9 8 1 1 1 5 10 8'.split()],
               reverse=True)

    res = []
    
    for element in a:
        try:
            res.append(b.pop(b.index(element + 1)))
        except ValueError:
            arr = [x for x in b if x > element]
            if arr:
                value = min(arr)
                if value:
                    res.append(value)
                    b.remove(value)

    return len(res)


def t(a, b):
    a = sorted([int(x) for x in a])
    b = sorted([int(x) for x in b])
    la = len(a) - 1
    lb = len(b) - 1
    count = 0
    for i in range(la, -1, -1):
        if b[lb] >= a[i]:
            count += 1
            a.pop(i)
            b.pop(lb)
            lb -= 1
        if lb < 0:
            break
    return count

if __name__ == "__main__":
    a = '8 2 4 7 8 5 5 8 6 9'.split()
    b = '9 8 1 1 1 5 10 8 2 7 4 3 15'.split()
    print(t(a, b))