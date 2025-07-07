def sort_template(mes_len: int, messages: list[int],
                  len_temp: int, templates: list[int]) -> str:
    result = []
    for filter in templates:
        result += [str(x) for x in messages if x == filter]
    t = sorted([value for value in messages if value not in templates])
    t1 = [str(x) for x in t]
    result.extend(t1)
    return ' '.join(result)


if __name__ == "__main__":
    print(sort_template(
        int(input()),
        [int(x) for x in input().split()],
        int(input()),
        [int(x) for x in input().split()]
    )
    )
    print(sort_template(
            11, [int(x) for x in '2 3 1 3 2 4 6 7 9 2 19'.split()],
            6, [int(x) for x in '2 1 4 3 9 6 0 0 0 0 0'.split()]
        )
    )


"""
2 3 1 3 2 4 6 7 9 2 19  # Номера контейнеров в грузовике.

2 1 4 3 9 6  # Шаблон-инструкция

2 2 2 1 4 3 3 9 6 7 19  # Результат работы робота-грузчика.

# Контейнеры 7 и 19 не были упомянуты в инструкции.
# Они переставлены в конец результирующего массива
# и отсортированы от меньшего к большему.
# И это правильно, так и надо.
"""
