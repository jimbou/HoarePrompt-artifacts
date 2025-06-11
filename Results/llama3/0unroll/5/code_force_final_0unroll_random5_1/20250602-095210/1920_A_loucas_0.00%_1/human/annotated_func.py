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
        
    #State: The loop will print the smallest number between the maximum of big and the minimum of less that is not in no for each test case. The loop will execute for the number of test cases equal to the value of `loop`. The value of `loop` will remain unchanged after the loop execution. The stdin will be empty after the loop execution.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers. It categorizes these integers into three lists based on their first value (1, 2, or 3), then finds and prints the smallest number between the maximum of the first category and the minimum of the second category that is not present in the third category. This process is repeated for each test case, leaving the input stream empty afterwards.

