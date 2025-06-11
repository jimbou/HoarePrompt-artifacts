#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: The output state is the sum of the least common multiple of each test case's integers, printed on separate lines. The value of `t` remains unchanged, and the contents of stdin are consumed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the sum of the least common multiple of each test case's integers and prints the result for each test case on separate lines. The function consumes the contents of standard input and does not modify the value of the initial input t.

