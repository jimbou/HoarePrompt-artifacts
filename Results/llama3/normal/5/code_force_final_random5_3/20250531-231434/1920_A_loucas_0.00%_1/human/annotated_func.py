#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
        for i in range(max(big), min(less)):
            if i not in no:
                num = i
                break
        
        print(num)
        
    #State: loop is 0, iterable is loop, stdin contains multiple test cases minus innerLoop test cases, less is a list containing innerLoop integers, big is a list that must have at least one element, no is an empty list, num is equal to the last value of i if i is not in no, otherwise num remains 0, innerLoop is an integer, iterable2 is innerLoop - 1, x is an integer, a is an integer, and the value of num is being printed, where num is either the last value of i if i is not in the empty list no, or 0 if i is in the empty list no

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers. It categorizes the integers into three lists based on their values and then finds the smallest integer that is not in the third list and is within the range of the maximum value in the first list and the minimum value in the second list. If such an integer is found, it prints the value; otherwise, it prints 0. The function repeats this process for all test cases.

