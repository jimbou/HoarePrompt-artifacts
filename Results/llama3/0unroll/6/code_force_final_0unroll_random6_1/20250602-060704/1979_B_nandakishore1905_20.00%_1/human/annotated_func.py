#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers x and y such that 0 <= x, y <= 10^9 and x != y.
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: The output state will contain the results of the given operations for each test case. For each test case, if the absolute difference between the two input numbers is a power of 2, the output will be the absolute difference. If the first number is 0 and the second number is odd, the output will be 1. If the first number is 0 and the second number is even, the output will be 2. For all other cases, the output will be the absolute difference minus the largest power of 2 that is less than or equal to the absolute difference.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two space-separated integers. It calculates the absolute difference between the two numbers and then applies specific rules to determine the output for each test case. If the absolute difference is a power of 2, it outputs the difference. If the first number is 0 and the second number is odd, it outputs 1. If the first number is 0 and the second number is even, it outputs 2. For all other cases, it outputs the absolute difference minus the largest power of 2 that is less than or equal to the absolute difference. The function prints the results for each test case.

