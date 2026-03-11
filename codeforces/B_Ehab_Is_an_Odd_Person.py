def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    even = False
    odd = False
    for i in range(n):
        if arr[i] % 2 == 0:
            even = True
        else:
            odd = True
    
    if even and odd:
        arr.sort()
    
    print(*arr)
solve()