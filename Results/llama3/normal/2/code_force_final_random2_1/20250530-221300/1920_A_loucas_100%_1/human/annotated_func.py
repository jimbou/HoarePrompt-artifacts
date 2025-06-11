#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
    #State: loop is 0, iterable is loop-1, innerLoop is an integer greater than or equal to 0, iterable2 is innerLoop, x is an integer, a is an integer, i is the last element in the list no, no is a list containing one or more integers a, less is a list containing one or more integers a, big is a list containing one or more integers a, stdin contains no input. If i is less than or equal to the minimum value in the list less and greater than or equal to the maximum value in the list big, then num is decreased by 1. Otherwise, num remains unchanged. The value of num is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of two integers each. It categorizes the integers into three lists based on their values, calculates the range of possible values between the minimum of one list and the maximum of another, and then subtracts the count of integers from the third list that fall within this range. The function prints the resulting count for each test case.

