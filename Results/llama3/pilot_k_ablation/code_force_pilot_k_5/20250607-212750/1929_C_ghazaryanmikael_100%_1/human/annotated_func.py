#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t sets of three space-separated integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: k is an integer, x is greater than or equal to 0, a is an integer, s is increased by at least x times s // (k - 1) + 1, i is x, stdin is empty, and 'YES' is printed if a is greater than or equal to s, otherwise 'NO' is printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers: k, x, and a. It then calculates a value s by iteratively adding s // (k - 1) + 1 to itself x times, starting from an initial value of 1. The function prints 'YES' if the calculated value s is less than or equal to a, and 'NO' otherwise. The function repeats this process for each test case in the input, until the input is exhausted.

