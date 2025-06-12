#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: stdin is empty, k, x, and a are undefined, s is undefined, and either 'YES' or 'NO' has been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers k, x, and a. For each test case, it calculates a value s based on k and x, and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. After processing all test cases, the function leaves the standard input empty and prints a 'YES' or 'NO' result for each test case.

