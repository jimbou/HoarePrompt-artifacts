#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: t is a positive integer, i is equal to t - 1, n is a positive integer between 1 and 2 * 10^6, m is a positive integer between 1 and 2 * 10^6, count is equal to m + 1, ans is equal to n + sum(g / count + 1) from count = 2 to m, g is n / m - (m - 1), and the integer value of ans which is equal to n + sum(g / count + 1) from count = 2 to m is being printed, and stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates a value 'ans' for each test case, which is initially set to n and then incremented by the sum of g / count + 1 for count from 2 to m, where g is n / count - (count - 1). The function prints the integer value of 'ans' for each test case. After processing all test cases, the function leaves the standard input empty.

