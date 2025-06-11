#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the values of X for each test case). The number of test cases is a positive integer and the values of X are integers such that 2 <= X <= 10^18.
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = ''
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        
        print(t)
        
        print(*ans)
        
    #State: i is equal to the initial number of test cases, x is 1, t is the number of times the loop executes, max is the original value of max minus the number of times the loop executes when x is even, min is the original value of min plus the number of times the loop executes when x is odd, ans is a string containing the values of max and min in the order they were appended, stdin contains no inputs, and the number of times the loop executes which is equal to t is being printed, and the values of max and min in the order they were appended are being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case is an integer X. For each test case, it repeatedly applies a transformation to X until it becomes 1, keeping track of the number of transformations and the values of a maximum and minimum counter. The function then prints the number of transformations and the sequence of maximum and minimum counter values in the order they were generated. The function processes all test cases and does not return any value.

