#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two distinct non-negative integers x and y. The number of test cases is specified in the first line of the input.
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif k % 2 != 0:
            print(1)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            f = k - q
            while f & f - 1 != 0:
                l = bin(f).replace('0b', '')
                p = len(l)
                q = 2 ** (p - 1)
                f = f - q
            print(f)
        
    #State: The output state will be a list of integers, where each integer is the result of the calculation for each test case. The calculation is based on the absolute difference between the two input integers, and it follows these rules: if the difference is a power of 2, it prints the difference; if the difference is odd, it prints 1; otherwise, it subtracts the largest power of 2 that is less than or equal to the difference, and repeats this process until the result is a power of 2, then prints the result.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains two distinct non-negative integers. It calculates the absolute difference between the two integers and applies a set of rules to determine the output: if the difference is a power of 2, it prints the difference; if the difference is odd, it prints 1; otherwise, it repeatedly subtracts the largest power of 2 that is less than or equal to the difference until the result is a power of 2, then prints the result. The function outputs a list of integers, where each integer is the result of the calculation for each test case.

