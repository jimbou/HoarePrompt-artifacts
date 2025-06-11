#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times.
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: `n` is a positive integer, `a` is an empty list, `cnt` is a list of `n + 1` integers where the value at each index `i` is equal to the number of occurrences of `i` in `a`, `x` is the last element of `cnt`, `ans` is the sum of `max(0, cnt[i] - 1)` for all `i` from 0 to `n`, `stdin` is empty, `input` is assigned to `sys.stdin.readline`, and `_` is the number of test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n integers. It then counts the occurrences of each integer in the list and calculates the sum of the counts minus one for each integer that appears more than once. The function prints this sum for each test case.

