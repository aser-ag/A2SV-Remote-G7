def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        # arr.sort()

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key

        flag = True
        for i in range(1, n):
            if arr[i] - arr[i - 1] > 1:
                flag = False
                break
        
        if flag:
            print("YES")
        else:
            print("NO")

solve()