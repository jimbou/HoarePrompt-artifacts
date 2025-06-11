#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a positive integer t (1 <= t <= 10^4). Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: t is a positive integer between 1 and 10^4, i is t - 1, n is an integer, m is an integer, count is m + 1, ans is n + sum(int(n / count) + 1) from count = 2 to m, countmins is m - 1, g is int(n / m) - m + 1, and the integer part of ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It then calculates and prints the sum of the integer divisions of n by all integers from 2 to m, inclusive, plus n. The function iterates over each test case, performing the calculation and printing the result for each case.

