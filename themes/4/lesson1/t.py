def find_two_indexes(data, expected_sum):
    # Ваше решение?
    l: list[int] = []
    for i in data:
        for j in data:
            if i + j == expected_sum and i != j:
                l.append((i, j))
    return l


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
