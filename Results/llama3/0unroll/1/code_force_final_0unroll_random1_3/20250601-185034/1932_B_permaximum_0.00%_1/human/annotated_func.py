#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: The output state will contain `t` lines, each representing the calculated `year` for each test case. The `year` is calculated by iterating over the `n` integers in each test case, adding the least common multiple of the current `year` and the current integer `ai` to `year`. The final `year` for each test case is printed on a new line.

#Overall this is what the function does:Calculates and prints the least common multiple (LCM) of a series of integers for multiple test cases. The function accepts no parameters and returns no value, instead printing the calculated LCM for each test case to the standard output. The input is expected to be provided through the standard input, with the number of test cases and the integers for each test case specified in a specific format.

