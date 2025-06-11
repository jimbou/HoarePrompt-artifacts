#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a, where k is an integer between 2 and 30, x is an integer between 1 and 100, and a is an integer between 1 and 10^9.
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 0
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: stdin is empty, `_` is the number of test cases, `k`, `x`, `a`, `s`, and `i` are undefined (since they are local to the loop and do not retain their values after the loop finishes), and either 'YES' or 'NO' has been printed for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. After processing all test cases, the function leaves the standard input empty and prints a 'YES' or 'NO' result for each test case.

