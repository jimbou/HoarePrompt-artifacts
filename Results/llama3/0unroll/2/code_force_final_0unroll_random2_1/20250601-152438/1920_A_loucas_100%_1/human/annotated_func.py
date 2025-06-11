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
        
        num = min(less) - max(big) + 1
        
        if num < 1:
            print(0)
            continue
        
        for i in no:
            if i <= min(less) and i >= max(big):
                num -= 1
        
        print(num)
        
    #State: Output State: The loop will execute 'loop' number of times, each time taking an integer 'innerLoop' as input and then 'innerLoop' number of pairs of integers as input. For each pair, it will categorize the integers into three lists based on the value of the first integer in the pair. It will then calculate the difference between the minimum value in the 'less' list and the maximum value in the 'big' list, add 1 to it, and store it in 'num'. If 'num' is less than 1, it will print 0 and move to the next iteration. Otherwise, it will subtract the count of numbers in the 'no' list that fall within the range of 'min(less)' and 'max(big)' from 'num' and print the result. The output will be 'loop' number of integers, each representing the count of numbers in the 'no' list that do not fall within the range of 'min(less)' and 'max(big)' for each iteration.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it categorizes input pairs of integers into three lists based on the first integer's value (1, 2, or 3). It then calculates the range between the minimum value in the 'less' list and the maximum value in the 'big' list, adjusts this range by 1, and subtracts the count of numbers in the 'no' list that fall within this range. The function prints the resulting count for each test case, which represents the number of integers in the 'no' list that do not fall within the calculated range. If the calculated range is less than 1, it prints 0 for that test case.

