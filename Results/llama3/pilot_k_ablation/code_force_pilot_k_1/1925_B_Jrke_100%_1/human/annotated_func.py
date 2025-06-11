#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
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
        
    #State: stdin is empty, t is an integer between 1 and 10^3, x and n are not defined, k is not defined, ans is not defined, and t lines have been printed, each containing the maximum divisor of the corresponding x that is less than or equal to the integer division of x by n.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers x and n. For each case, it calculates and prints the maximum divisor of x that is less than or equal to the integer division of x by n. The function processes all test cases and prints the results, leaving the standard input empty after execution.

