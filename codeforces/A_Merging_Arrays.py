def solve():
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    a1, a2 = 0, 0
    final = []

    while a1 < n and a2 < m:
        if arr1[a1] < arr2[a2]:
            final.append(arr1[a1])
            a1 += 1
        else:
            final.append(arr2[a2])
            a2 += 1
    
    if a1 < n:
        final.extend(arr1[a1:])

    if a2 < m:
        final.extend(arr2[a2:])
    
    
    print(*final)

solve()