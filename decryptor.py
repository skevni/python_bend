# contestID=139229204
def decryptor(message: str) -> str:
    stack = []
    decrypted_command = ''
    factor = ''
    numbers = '0123456789'
    for char in message:
        match char:
            case _ if char in numbers:
                factor += char
            case '[':
                stack.append(
                    (int(factor),
                        decrypted_command)
                )
                decrypted_command, factor = '', ''
            case ']':
                repeat, precommand = stack.pop()
                decrypted_command = precommand + repeat * decrypted_command
            case _:
                decrypted_command += char

    return decrypted_command


if __name__ == "__main__":
    print(decryptor(input()))
