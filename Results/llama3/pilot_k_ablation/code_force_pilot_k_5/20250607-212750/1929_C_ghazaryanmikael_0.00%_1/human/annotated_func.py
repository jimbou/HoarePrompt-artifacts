#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a, where k is an integer between 2 and 30 (inclusive), x is an integer between 1 and 100 (inclusive), and a is an integer between 1 and 10^9 (inclusive).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 0
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: k is an integer, x is 0, a is an integer, s is increased by s // (k - 1) + 1 x times, i is 0, stdin is empty, and either 'YES' is printed if a is greater than or equal to s or 'NO' is printed if a is less than s.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing three integers k, x, and a. It calculates a value s by repeatedly adding s // (k - 1) + 1 to itself x times. The function then prints 'YES' if a is greater than or equal to the calculated value s, and 'NO' otherwise. After processing all test cases, the function leaves the standard input empty.

