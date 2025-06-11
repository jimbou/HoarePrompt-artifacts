#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 1000) and then t integers (2 ≤ X ≤ 10^18).
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
        
    #State: t is the number of times the loop executes, i is t-1, x is 1, ans is a string containing the sequence of numbers from min to -1, max is 100000000, min is -100000000, and stdin contains no integer inputs.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer (x) is a number to be processed. For each x, the function generates a sequence of numbers by repeatedly dividing x by 2 if it's even or subtracting 1 if it's odd, until x becomes 1. The function then prints the number of steps taken to reach 1 and the generated sequence of numbers. The function processes all test cases and does not return any value.

