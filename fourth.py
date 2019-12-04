start = 100000
end = 200000


def contains_double(password):
    for i in range(len(password) - 1):
        first = password[i]
        second = password[i + 1]
        if first == second:
            return True
    return False


def increasing(password):
    for i in range(len(password) - 1):
        first = password[i]
        second = password[i + 1]
        if first > second:
            return False
    return True


if __name__ == '__main__':
    password = str(start)
    matchingPasswords = []
    while int(password) < end:
        if contains_double(password) and increasing(password):
            matchingPasswords.append(password)
        password = str(int(password) + 1)
    print('found:', len(matchingPasswords), 'matching passwords.')
