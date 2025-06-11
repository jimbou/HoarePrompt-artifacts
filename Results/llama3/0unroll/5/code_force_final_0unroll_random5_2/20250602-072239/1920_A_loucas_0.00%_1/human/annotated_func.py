#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9). a denotes the type of constraint. If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x.
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
        
    #State: The loop will execute 'loop' number of times, and for each iteration, it will print the smallest number between the maximum of 'big' and the minimum of 'less' that is not in 'no'. The state of 'loop' and other variables not affected by the loop will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer n followed by n lines of two integers a and x. It then determines the smallest number k that satisfies the constraints provided by the input, where k must be greater than or equal to x if a=1, less than or equal to x if a=2, and not equal to x if a=3. The function prints the smallest such k for each test case.

