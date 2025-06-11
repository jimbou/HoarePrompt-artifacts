#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n lines, each containing two integers a and x (a in {1,2,3}, 1 <= x <= 10^9).
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
        
    #State: The loop will execute `loop` number of times. In each iteration, it will read `innerLoop` number of lines from stdin, where `innerLoop` is an integer between 2 and 100 (inclusive). For each line, it will read two integers `x` and `a`, where `x` is either 1, 2, or 3, and `a` is an integer between 1 and 10^9 (inclusive). The loop will then process these inputs and print an integer `num` to stdout. After all iterations, the loop will finish, and the program will terminate. The state of the other variables in the precondition that are not affected by the loop head and body will remain unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a number of lines, each containing two integers. It categorizes these integers into three groups based on their first value (1, 2, or 3), and then finds the smallest integer that is not present in the third group and is within the range of the maximum value in the first group and the minimum value in the second group. It prints this integer to standard output for each test case.

