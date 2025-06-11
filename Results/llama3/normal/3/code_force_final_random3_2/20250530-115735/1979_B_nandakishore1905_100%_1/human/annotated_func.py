#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated non-negative integers x and y, where x is not equal to y. The number of test cases is specified by an integer t in the first line of stdin, where 1 <= t <= 10^4.
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
        
    #State: i equals the number of test cases, stdin is empty, n and m are the last test case integers, k is the absolute difference between n and m, and the output is a sequence of numbers, each of which is either the absolute difference between two test case integers if it is a power of 2, 1 if the absolute difference is odd, or a power of 2 if the absolute difference is even but not a power of 2.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two space-separated non-negative integers. It calculates the absolute difference between these integers and prints a value based on whether this difference is a power of 2, odd, or an even number that is not a power of 2. If the difference is a power of 2, it prints the difference. If the difference is odd, it prints 1. If the difference is even but not a power of 2, it prints the largest power of 2 that is less than or equal to the difference. The function continues this process until all test cases have been read from standard input, at which point the input is exhausted.

