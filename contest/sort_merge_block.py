def main(data_len: int, data: list[str]):
    sum_data = block_counts = sum_index = 0
    for index in range(data_len):
        sum_index += index
        sum_data += int(data[index])
        if sum_data == sum_index or index == data_len:
            block_counts += 1
            sum_data = sum_index = 0
    return block_counts


if __name__ == '__main__':
    # print(main(int(input()), [int(x) for x in input().split()]))
    d = '3 6 7 4 1 5 0 2'.split()
    print(main(8, d))

# 3 1 0 2 | 6 5 4 | 7  блоков 3
# 0 1 3 2 блоков 3

# 1 0 2 3 4 блоков 4

# 3 6 7 4 1 5 0 2 блоков 1

# 3 6 7 0 4 2 1 5   блоков 1
# 3 0 4 2 1 6 7 5   блоков 2

# 4 7 3 5 6 1 0 2

#len=4, arr: 0 3 2 1 4      ret=2

# 2 0 1 4 3
