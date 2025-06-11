#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: t is an integer between 0 and 1000 inclusive, stdin contains 0 test cases, n is an integer between 1 and 100 inclusive, a is an empty list, ai is undefined, year is equal to the sum of all elements in the initial list a plus the sum of all elements in the initial list a modulo each element in the initial list a or each element in the initial list a, and _ is equal to the initial value of t, and the value of year is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates a value 'year' for each test case by summing the integers and adding the sum of the remainders when the sum is divided by each integer. The function then prints the calculated 'year' value for each test case.

