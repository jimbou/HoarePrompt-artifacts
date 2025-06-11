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
        
    #State: t is an integer greater than or equal to 0, i is t, n is an integer, m is an integer, count is m + 1, ans is n + sum(int(g / count) + 1 for count in range(2, m + 1)), countmins is m - 1, g is int(n / m) - (m - 1), and the integer value of ans is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and m. It calculates a value 'ans' based on the given formula and prints the integer value of 'ans' for each test case. The function iterates over the range from 2 to m (inclusive), updating 'ans' by adding the integer division of 'g' by the current count, where 'g' is calculated as 'n' divided by the current count minus the count minus one. The function breaks the loop if 'g' becomes less than the count minus one. The final state of the program is that the integer value of 'ans' is printed for each test case.

