def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    # print(*arr)
    if k == 0:
        x = arr[0] - 1
        if x < 1:
            x = -1
        print(x)
    else:
        if k == n:
            print(arr[-1])
        elif arr[k] == arr[k - 1]:
            print(-1)
        else:
            print(arr[k - 1])
    



solve()
