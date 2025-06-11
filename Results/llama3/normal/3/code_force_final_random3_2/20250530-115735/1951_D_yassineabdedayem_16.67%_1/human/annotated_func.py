#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^18) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end.
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
        
    #State: t is 0, n is 0, k is greater than or equal to 0, rep is less than 61, tab is a list containing a string element for each iteration of the loop. If k is 0, then 'YES' is printed, the length of the tab list which is less than 61 is printed, and all elements of the tab list which are i are printed. Otherwise, 'NO' is printed, Min is the minimum of n // k and k, Max is the maximum of int(n / k) and k. If Max equals k and n * Min is less than or equal to k, then number is the minimum of n // k and k, and k is decreased by the maximum of n / k and k. Otherwise, number is the maximum of n / k and k, and k is decreased by Min.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two positive integers, n and k. It attempts to find a sequence of numbers that can be used to make k jewels with n coins. If such a sequence is found, it prints 'YES', the length of the sequence, and the sequence itself. If no sequence is found, it prints 'NO'. The function repeats this process for all test cases provided in the input.

