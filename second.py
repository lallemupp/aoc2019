from enum import IntEnum

int_code = [2,4,4,5,99,0]


class Operators(IntEnum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


def add(first_index, second_index, store_index):
    first = int_code[first_index]
    second = int_code[second_index]
    result = first + second
    int_code[store_index] = result


def multiply(first_index, second_index, store_index):
    first = int_code[first_index]
    second = int_code[second_index]
    result = first * second
    int_code[store_index] = result


if __name__ == '__main__':
    i = 0
    while True:
        operator = int_code[i]
        i += 1
        if operator == Operators.HALT:
            print('done')
            break
        first = int_code[i]
        i += 1
        second = int_code[i]
        i += 1
        store = int_code[i]
        i += 1
        if operator == Operators.ADD:
            add(first, second, store)
        elif operator == Operators.MULTIPLY:
            multiply(first, second, store)
        else:
            print("got an invalid operator:", operator)
            exit(1)
    print(int_code)
