import time


def fibonachi(n):
    if n >= 0 and n <= 1:
        return n
    else:
        return fibonachi(n - 2) + fibonachi(n - 1)


def fibonachi_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


current_time = time.time()
print(fibonachi(30))
print('Recursive method takes {time.time() - current_time} sec.')
current_time = time.time()
print(fibonachi_iterative(30))
print('Recursive method takes {time.time() - current_time} sec.')

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1001)
