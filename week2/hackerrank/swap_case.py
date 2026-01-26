def swap_case(s):
    result = []
    for letter in s:
        if letter.isupper():
            result.append(letter.lower())
        else:
            result.append(letter.upper())
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)