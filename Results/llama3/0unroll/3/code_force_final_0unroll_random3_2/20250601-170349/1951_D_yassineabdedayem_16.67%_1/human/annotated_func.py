#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000) — the number of test cases. Each of the following t lines contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        rep = 0
        
        number = 0
        
        tab = []
        
        while n != 0 and k > 0 and rep < 60 and n >= k:
            Min, Max = min(n // k, k), max(int(n / k), k)
            if Max == k and n * Min <= k:
                number = Min
                k = k - Max
            else:
                number = Max
                k = k - Min
            tab.append(str(number))
            n -= Min * Max
            rep += 1
        
        if k == 0:
            print('YES')
            print(len(tab))
            for i in tab:
                print(i, end=' ')
        else:
            print('NO')
        
    #State: The output state is a series of 'YES' or 'NO' statements, each followed by either a sequence of numbers or nothing, depending on whether the loop was able to find a valid sequence of jewel purchases for Alice. The number of 'YES' or 'NO' statements is equal to the initial value of `t`. The stdin is empty, having been fully read by the loop. The value of `t` is unchanged, as it is not modified within the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two positive integers, n and k. For each test case, it attempts to find a sequence of jewel purchases that Alice can make to end up with k jewels, given that she starts with n coins. If a valid sequence is found, it prints 'YES' followed by the length of the sequence and the sequence itself. If no valid sequence is found, it prints 'NO'. The function continues this process until all test cases have been processed, at which point the standard input is empty.

