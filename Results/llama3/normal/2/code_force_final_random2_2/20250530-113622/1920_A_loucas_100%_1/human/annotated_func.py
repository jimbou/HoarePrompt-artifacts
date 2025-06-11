#State of the program right berfore the function call: stdin contains multiple test cases. Each test case starts with an integer n (2 <= n <= 100), followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
    #State: `loop` is an integer between 2 and 100, `iterable` is `loop - 1`, `innerLoop` is an integer, `iterable2` is `innerLoop - 1`, `x` is an integer, `a` is an integer, `num` is at least -len(no), `no` is a list containing at least len(no) integers, `i` is the last element in `no`, and `stdin` contains no input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n lines of two integers each. It categorizes the integers into three lists based on their values, calculates the range of possible values between the minimum of one list and the maximum of another, and then subtracts the count of integers from the third list that fall within this range. The function prints the result for each test case, which represents the number of possible values that do not overlap with the integers in the third list.

