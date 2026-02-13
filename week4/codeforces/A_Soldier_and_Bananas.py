def solve():
    cost, dollars, amount = map(int, input().split())
    total = 0

    for i in range(1, amount + 1):
        current = cost * i
        total += current
    
    if total > dollars:
        print(total - dollars)
    else:
        print(0)

solve()
# 3, 6, 9, 12