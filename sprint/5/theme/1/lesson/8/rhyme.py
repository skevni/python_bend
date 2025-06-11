# Реализация считалки
# Задается кол-во игроков и второй параметр на каком шаге выбывает игрок.
# Выводим того, кто остался

def get_looser(users_count, takt, index=0):
    users = list(range(1, users_count+1))
    dropped = 0
    for _ in range(users_count - 1):
        start = dropped % len(users)
        dropped = (start + takt - 1) % len(users)
        print(f'Remove {users[dropped]}')
        users.pop(dropped)
    return users.pop()


if __name__ == "__main__":
    applicants = int(input())
    takts = int(input())
    print(get_looser(applicants, takts))


# 1 2 3 4 5
# 2