#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: The loop has executed t times, and for each iteration, the output is either 'YES' with two numbers, or 'NO'. The value of t is not changed, and the stdin contains no test cases.

#Overall this is what the function does:Determines whether it's possible for Alice to buy a certain number of jewels with her coins and prints the result along with the minimum number of coins needed to buy the jewels if possible, or 'NO' if not.

