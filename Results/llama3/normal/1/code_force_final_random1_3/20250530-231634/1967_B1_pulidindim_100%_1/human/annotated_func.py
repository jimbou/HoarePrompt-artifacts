#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two integers n, m (1 <= n, m <= 2 * 10^6).
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
        
    #State: t is an integer between 0 and 10^4 (inclusive), i is t, n is an integer, m is an integer, count is m + 1, ans is n + sum(int(g / count) + 1 for count in range(2, m + 1)), countmins is m - 1, g is int(n / m) - countmins, and the integer value of ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and m. It then calculates and prints the sum of the integer divisions of n by all integers from 2 to m (inclusive), plus n, for each test case. The function iterates through each test case, performing the calculation and printing the result.

