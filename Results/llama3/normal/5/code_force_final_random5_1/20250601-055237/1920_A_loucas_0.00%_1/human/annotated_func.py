#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n followed by n lines, each containing two integers a and x. a is 1, 2, or 3, and 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2. No two constraints are the exact same.
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
        
    #State: loop is 0, iterable is equal to loop, iterable2 is equal to innerLoop, x is an integer from the input, a is an integer from the input, big is a non-empty list containing integers from the input if x is 1 and a, less is a non-empty list containing integers from the input if x is 2 and a, no is a list containing integers from the input if x is not 1 or 2 and a, num is equal to the first integer in the range from max(big) to min(less) that is not in the list no, innerLoop is the first integer n from the first test case, and stdin contains multiple test cases (with the first test case partially read).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It categorizes the integers into three lists based on the value of a (1, 2, or 3), and then finds the first integer in the range from the maximum of the first list to the minimum of the second list that is not present in the third list. The function prints this integer for each test case.

