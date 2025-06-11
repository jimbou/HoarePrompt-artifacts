#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with an integer n (2 <= n <= 100), followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9). The first integer t (1 <= t <= 500) represents the number of test cases.
    loop = int(input())
    for iterable in range(loop):
        less = []
        
        big = []
        
        no = []
        
        num = 0
        
        innerLoop = int(input())
        
        for iterable2 in range(innerLoop):
            x, a = map(int, input().split())
            if x == 1:
                big.append(a)
            elif x == 2:
                less.append(a)
            else:
                no.append(a)
        
        num = min(less) - max(big) + 1
        
        if num < 1:
            print(0)
            continue
        
        for i in no:
            if i <= min(less) and i >= max(big):
                num -= 1
        
        print(num)
        
    #State: Output State: The output state after the loop executes all the iterations is a series of printed numbers, each representing the count of numbers that are within the range defined by the minimum of the 'less' list and the maximum of the 'big' list, minus the count of numbers in the 'no' list that fall within this range. The loop iterates 'loop' times, processing 'innerLoop' test cases in each iteration, where 'innerLoop' is the input integer read at the start of each iteration. The output is printed to the console, with each number on a new line.

#Overall this is what the function does:This function reads input from the console, processes multiple test cases, and prints the count of numbers within a specific range for each test case. It accepts no parameters and returns no values, instead, it prints the results directly to the console. The function iterates over the input test cases, categorizes numbers into three lists based on their values, calculates the range, and then adjusts the count by subtracting numbers that fall within the range from the 'no' list. The final state of the program is a series of printed numbers, each representing the adjusted count for a test case.

