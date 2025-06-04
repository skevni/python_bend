import os


CURRENT_PATH = os.path.dirname(__file__)


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def peek(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack[-1]

    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    def size(self):
        return len(self.__stack)


def main():
    with open(os.path.join(CURRENT_PATH, 'input.txt'), 'r') as fi:
        line = fi.readline().strip()
        stack = Stack()
        for char in line:
            if char == ']':
                if stack.peek() == '[':
                    stack.pop()
                else:
                    return False
            elif char == ')':
                if stack.peek() == '(':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if stack.peek() == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.push(char)

        return True if stack.size() == 0 else False


if __name__ == "__main__":
    with open(os.path.join(CURRENT_PATH, 'output.txt'), 'w') as fo:
        fo.write(str(main()))
