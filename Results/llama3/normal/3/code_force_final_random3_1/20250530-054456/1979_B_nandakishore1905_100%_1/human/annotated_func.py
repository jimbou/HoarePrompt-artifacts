#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two distinct non-negative integers x and y (0 <= x, y <= 10^9, x != y).
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
        
    #State: i is t-1, n is an integer, m is an integer, k is the absolute difference between n and m, stdin contains multiple lines of input minus t lines. If the absolute difference between n and m, which is k, is a power of 2, then k is printed. Otherwise, if k is odd, 1 is printed, and if k is even but not a power of 2, a power of 2 is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each of the following t lines contains two distinct non-negative integers x and y. It calculates the absolute difference k between x and y for each pair, and then prints k if it's a power of 2, 1 if k is odd, or the largest power of 2 less than k if k is even but not a power of 2. The function processes t pairs of integers and prints a corresponding value for each pair.

