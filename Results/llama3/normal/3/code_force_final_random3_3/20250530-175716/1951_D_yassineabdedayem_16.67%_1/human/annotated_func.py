#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
        
    #State: t is 0, n is 0, rep is 60, tab is a list containing the string representation of number, number is the maximum of int(n / k) and k, stdin is empty. If k is 0, 'YES' is being printed, and the 60th string representation of a number in the list is being printed 60 times followed by a space. If k is not equal to 0, 'NO' is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and k. It attempts to find a sequence of numbers that can be used to make k jewels with n coins, following certain rules. If a valid sequence is found, it prints 'YES' followed by the length of the sequence and the sequence itself. If no valid sequence is found, it prints 'NO'. The function processes all test cases and then terminates, leaving the standard input empty.

