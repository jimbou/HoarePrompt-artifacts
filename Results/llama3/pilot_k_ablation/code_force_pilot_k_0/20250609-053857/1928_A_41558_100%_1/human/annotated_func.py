#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers a and b (1 <= a, b <= 10^9).
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: The loop will print 'YES' or 'NO' for each test case, indicating whether the given numbers a and b can be transformed into each other by a sequence of operations where a number is either doubled or halved, with the constraint that the number must be odd when doubled or even when halved. The output will be a sequence of 'YES' or 'NO' for each test case, without any additional information.

#Overall this is what the function does:Determines whether two given integers can be transformed into each other by a sequence of doubling or halving operations, with the constraint that a number must be odd when doubled or even when halved, and prints 'YES' or 'NO' for each test case.

