"""
10
8 2 4 7 8 5 5 8 6 9
13
9 8 1 1 1 5 10 8 2 7 4 3 15
"""

def t():
    a = [int(x) for x in '8 2 4 7 8 5 5 8 6 9'.split()]
    b = sorted([int(x) for x in '9 8 1 1 1 5 10 8 2 7 4 3 15'.split()])

    res = []
    
    for element in a:
        try:
            res.append(b.pop(b.index(element + 1)))
        except ValueError:
            value = min([x for x in b if x > element])
            if value:
                res.append(value)
                b.remove(value)

    return len(res)


if __name__ == "__main__":
    print(t())