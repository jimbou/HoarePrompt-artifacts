#State of the program right berfore the function call: stdin contains multiple inputs: first an integer (the number of test cases), then for each test case, first an integer (the length of the strip) and then a string of 'W's and 'B's of the same length.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: Output State: The output will be the minimum number of 'B's that need to be painted to make the strip look like it's made of 'W's for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the length of a strip) followed by a string of 'W's and 'B's. It then calculates and prints the minimum number of 'B's that need to be painted to make the strip look like it's made of 'W's for each test case. The function processes all test cases and outputs the minimum number of 'B's to be painted for each case.

