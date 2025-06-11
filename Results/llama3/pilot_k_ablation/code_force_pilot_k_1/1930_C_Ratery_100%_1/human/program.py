def solve() -> None:
    n = int(input())
    arr = list(map(sum, enumerate(map(int, input().split()), start=1)))
    arr.sort(reverse=True)
    ans = [arr[0]]
    for x in arr[1:]:
        if x >= ans[-1]:
            ans.append(ans[-1] - 1)
        else:
            ans.append(x)
    print(*ans)
 
 
for _ in range(int(input())):
    solve()