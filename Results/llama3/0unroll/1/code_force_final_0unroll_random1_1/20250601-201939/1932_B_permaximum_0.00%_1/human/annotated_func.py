#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: The output state will be the sum of the least common multiple (LCM) of each test case's integers, printed on separate lines. The LCM is calculated by adding the current year to the remainder of the year divided by each integer, or the integer itself if the remainder is zero. The final output will be a series of integers, each representing the total year after processing all integers in each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the least common multiple (LCM) of each test case's integers by iteratively adding the current year to the remainder of the year divided by each integer, or the integer itself if the remainder is zero. The function then prints the total year after processing all integers in each test case, resulting in a series of integers as output.

