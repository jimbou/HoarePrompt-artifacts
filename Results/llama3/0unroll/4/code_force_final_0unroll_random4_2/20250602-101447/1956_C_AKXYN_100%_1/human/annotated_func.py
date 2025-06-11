#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: The output state will contain the results of the loop's execution for each test case. For each test case, it will print the value of 'res' and 'n << 1', followed by 'n' lines of output, each containing the numbers from 1 to 'n' in ascending order, and then 'n' lines of output, each containing the numbers from 1 to 'n' in descending order.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n representing the size of a matrix. For each test case, it calculates a result 'res' based on the formula res += (i + 1) * (2 * i + 1) for i ranging from 0 to n-1, and then prints the value of 'res' and 'n << 1'. Additionally, it prints 'n' lines of output containing numbers from 1 to 'n' in ascending order, followed by 'n' lines of output containing numbers from 1 to 'n' in descending order.

