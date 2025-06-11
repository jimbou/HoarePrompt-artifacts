#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of lines, each containing two integers (the number of 1x1 icons and the number of 2x2 icons) separated by a space. The number of test cases is a positive integer and the number of icons are non-negative integers less than or equal to 99.
    ap = int(input())
    for k in range(ap):
        x, y = map(int, input().split())
        
        if x > 0 and y > 0:
            bxsfory = math.ceil(y / 2)
            x = x - bxsfory * 15 + y * 4
            bxsfory1 = 0 if x <= 0 else math.ceil(x / 15)
            print(bxsfory1 + bxsfory)
        elif x == 0 and y > 0:
            print(math.ceil(y / 2))
        elif x > 0 and y == 0:
            print(math.ceil(x / 15))
        else:
            print(0)
        
    #State: Output State: The loop has executed `ap` times, and for each iteration, the output is the total number of icons that can be placed on the screen, calculated based on the number of 1x1 and 2x2 icons provided as input. The output is printed to the console. The value of `ap` remains unchanged, and the stdin buffer is empty after all iterations.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers representing the number of 1x1 and 2x2 icons. It calculates the total number of icons that can be placed on the screen based on the provided numbers and prints the result to the console. The function handles four possible scenarios: both 1x1 and 2x2 icons are present, only 2x2 icons are present, only 1x1 icons are present, and neither type of icon is present. The function iterates over the specified number of test cases, processing each one independently and printing the corresponding output.

