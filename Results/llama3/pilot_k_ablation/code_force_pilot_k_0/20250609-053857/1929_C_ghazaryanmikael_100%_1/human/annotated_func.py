#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case. The number of 'YES' or 'NO' printed will be equal to the value of t in the initial state. Each 'YES' or 'NO' will indicate whether the value of a is greater than or equal to the calculated value of s for the corresponding test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers: k, x, and a. For each test case, it calculates a value s based on the given formula and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. The function repeats this process for the number of test cases specified by the initial integer t, printing one 'YES' or 'NO' for each test case.

