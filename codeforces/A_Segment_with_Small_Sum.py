def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = 0, 0
    sum = 0
    longest = 0
    for right in range(left, n):
        sum += arr[right]

        if sum <= s:
            current = right - left + 1
            longest = max(longest, current)
        else:
            while sum > s:
                    sum -= arr[left]
                    left += 1
    
    print(longest)

solve()