#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two distinct non-negative integers x and y (0 <= x, y <= 10^9).
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
        
    #State: The output state will be a series of integers, each representing the largest power of 2 that is less than or equal to the absolute difference between the two input integers. If the absolute difference is a power of 2, it will be printed as is. If the absolute difference is odd, 1 will be printed. Otherwise, the largest power of 2 that is less than or equal to the absolute difference will be printed.

#Overall this is what the function does:The function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains two distinct non-negative integers. It calculates the absolute difference between these integers, and then prints the largest power of 2 that is less than or equal to this difference. If the difference is a power of 2, it prints the difference as is. If the difference is odd, it prints 1. The function repeats this process for each test case, producing a series of integers as output.

