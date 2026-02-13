def solve():
    n = int(input())

    for i in range(n):
        word = input().strip()

        if len(word) > 10:
            abbr = []
            abbr.append(word[0])
            abbr.append(str(len(word) - 2))
            abbr.append(word[-1])
            print("".join(abbr))
        else:
            print(word)

solve()