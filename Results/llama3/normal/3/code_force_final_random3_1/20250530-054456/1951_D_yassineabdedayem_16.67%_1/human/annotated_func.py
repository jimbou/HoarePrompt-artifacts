#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and k (1 <= n, k <= 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
        
    #State: t is 0, _ is t, n is 0, number is either the minimum of n // k and k or the maximum of int(n / k) and k, rep is less than or equal to 60, tab is a list containing string representations of number, Min is the minimum of n // k and k, Max is the maximum of int(n / k) and k, and stdin contains no test cases. If k is 0, 'YES' is printed, the length of the tab list which is greater than or equal to 0 is printed, and all elements in the tab list are printed. If k is not equal to 0, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and k. It then attempts to find a sequence of numbers that can be used to make k jewels using n coins, with the goal of making k jewels. If successful, it prints 'YES' followed by the length of the sequence and the sequence itself. If it fails to find a sequence, it prints 'NO'. The function processes all test cases and prints the results accordingly.

