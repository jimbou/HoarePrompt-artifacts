#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
        
    #State: The output state after the loop executes all the iterations will be a series of 'YES' or 'NO' statements, followed by either one or two numbers, depending on the values of n and k. If n equals k, the output will be 'YES', followed by 1 and then 1. If n + 2 is greater than k * 2, the output will be 'YES', followed by 2, then n - k + 1, and finally 1. If neither of these conditions is met, the output will simply be 'NO'. The number of these outputs will be equal to the value of t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two positive integers, n and k. It then determines whether it's possible for Alice to buy a certain number of jewels with her coins, such that she ends up with exactly k jewels. If possible, it outputs 'YES' followed by the number of purchases needed and the number of coins spent in each purchase. If not possible, it outputs 'NO'. The function repeats this process for each test case, producing a series of 'YES' or 'NO' statements along with additional purchase information when applicable.

