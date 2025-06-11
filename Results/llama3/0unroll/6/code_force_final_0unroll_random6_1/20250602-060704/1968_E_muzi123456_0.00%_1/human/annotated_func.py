#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 50) followed by t positive integers n (2 <= n <= 10^3).
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: t = 0, n = last input integer, i = last value of n + 1

#Overall this is what the function does:The function reads a positive integer t from standard input, representing the number of test cases. For each test case, it reads a positive integer n and prints a sequence of numbers from 1 to n, with each number followed by its corresponding index (starting from 1). The function repeats this process t times, after which it terminates.

