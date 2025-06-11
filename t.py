# m = (0, 1)
# m1 = (20, 40)
# nt = tuple(sum(i) for i in zip(m, m1))
# print(nt)


print([
    chr(code) for code in range(10*256)
    if chr(code).isdigit()  # .isnumeric() .isdecimal()
])

print('߉'.isdigit())