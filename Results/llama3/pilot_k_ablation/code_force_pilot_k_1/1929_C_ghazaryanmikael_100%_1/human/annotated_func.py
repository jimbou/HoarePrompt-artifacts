#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 1000). Each of the following t lines contains three integers k, x and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: `stdin` is empty, `k`, `x`, `a`, and `s` are not defined, and either 'YES' or 'NO' has been printed for each of the initial t lines of input.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains three integers (k, x, and a). It then calculates a value (s) based on k and x, and prints 'YES' if a is greater than or equal to s, and 'NO' otherwise, for each test case. After processing all test cases, stdin is empty and the function has printed a 'YES' or 'NO' result for each test case.

