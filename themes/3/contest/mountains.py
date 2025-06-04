
from array import array
import os


CURRENT_PATH = os.path.dirname(__file__)


def main():
    input_array = array('b')

    with open(os.path.join(CURRENT_PATH, 'input.txt'), 'r') as fi:
        inputs = fi.readline().split()
        for i in inputs:
            input_array.append(int(i))
    if len(input_array) < 3:
        return False
    uptrend = False
    for ind in range(len(input_array) - 1):
        if ind > 0:
            if (input_array[ind] == input_array[ind - 1]
                    or input_array[ind] == input_array[ind + 1]):
                return False
            if input_array[ind] > input_array[ind - 1]:
                uptrend = True
                if (
                    ind == len(input_array) - 2
                    and input_array[ind + 1] > input_array[ind]
                ):
                    return False
            if (
                input_array[ind] < input_array[ind - 1]
                    and (input_array[ind] < input_array[ind + 1]
                         or not uptrend)
            ):
                return False

    return True


if __name__ == "__main__":
    with open(os.path.join(CURRENT_PATH, 'output.txt'), 'w') as fo:
        fo.write(str(main()))
