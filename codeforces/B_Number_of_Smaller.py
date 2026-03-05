def solve():
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    lessThan = 0
    result = []

    for i in range(m):
        while lessThan < n and arr1[lessThan] < arr2[i]:
            lessThan += 1

        result.append(lessThan)
    
    print(*result)

solve()