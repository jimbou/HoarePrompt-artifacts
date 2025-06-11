#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two integers n, m (1 <= n, m <= 2 * 10^6).
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
        
    #State: t is an integer between 0 and 10^4 (exclusive), i is equal to t, n is an integer between 1 and 2 * 10^6 (inclusive), m is an integer between 1 and 2 * 10^6 (inclusive), count is equal to m + 1, ans is an integer equal to n + sum(g / count + 1) from count = 2 to m, countmins is m - 1, g is an integer equal to n / m - countmins, and the integer value of ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and m. It calculates a value 'ans' based on the given formula and prints the integer value of 'ans' for each test case. The function iterates over each test case, performing calculations and printing the result, without modifying the input values.

