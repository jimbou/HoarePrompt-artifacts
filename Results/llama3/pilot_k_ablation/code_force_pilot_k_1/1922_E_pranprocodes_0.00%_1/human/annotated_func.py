#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the values of X).
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
        
    #State: `i` is equal to the number of test cases, `max` is 100000000, `min` is -100000000, `ans` is an empty string, `t` is 0, `x` is 1, and `stdin` is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer value. For each test case, it generates a sequence of numbers by repeatedly dividing the input number by 2 if it's even or subtracting 1 if it's odd, until the number becomes 1. The function then prints the length of this sequence and the sequence itself, with each number in the sequence being either the maximum possible value (100000000) if the corresponding operation was a division by 2, or the minimum possible value (-100000000) if the operation was a subtraction by 1. The function processes all test cases and then terminates, leaving the input stream empty.

