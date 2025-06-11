#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6). The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
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
        
    #State: t is a positive integer, i is t - 1, n is a positive integer, m is a positive integer, count is m + 1, ans is n + the sum of the series (n / k - (k - 1)) / k + 1 for k from 2 to m, countmins is m - 1, g is n / m - (m - 1), and the integer value of ans is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates a value 'ans' by adding a series of fractions to 'n', and then prints the integer value of 'ans'. The series is calculated by iterating from 2 to m, adding the result of the division of 'n' by the current number minus the current number minus one, divided by the current number plus one, to 'ans'. The function continues this process until it has processed all test cases.

