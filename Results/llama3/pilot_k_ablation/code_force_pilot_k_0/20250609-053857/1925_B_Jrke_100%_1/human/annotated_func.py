#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^3) followed by t lines, each containing two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: The output state will be the maximum number of factors that can be obtained from the given numbers x and n, for each test case. The output will be a series of integers, each representing the maximum number of factors for the corresponding test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers x and n. For each test case, it calculates the maximum number of factors that can be obtained from x, considering factors up to x/n, and prints the result. The function processes multiple test cases and outputs the maximum number of factors for each case.

