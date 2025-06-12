#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two distinct non-negative integers x and y (0 <= x, y <= 10^9, x != y).
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        
        l1, l2 = [], []
        
        while x:
            l1.append(x % 2)
            x //= 2
        
        while y:
            l2.append(y % 2)
            y //= 2
        
        if len(l2) < len(l1):
            l2.append(0)
        elif len(l1) < len(l2):
            l1.append(0)
        
        n = len(l1)
        
        if len(l2) < len(l1):
            n = len(l2)
        
        cnt = 0
        
        for i in range(n):
            if l1[i] == l2[i]:
                cnt += 1
            else:
                break
        
        print(2 ** cnt)
        
    #State: `t` is an integer between 1 and 10^4, stdin contains 0 lines of input, _ is t-1, the current value of x is 0, the current value of y is 0, l1 is a list containing the binary representation of the last value of x, l2 is a list containing the binary representation of the last value of y in reverse order. The length of l1 is either equal to the length of l2, or l1 has an additional element 0 appended to it if the original length of l2 was more than the length of l1. If the length of l2 is less than the length of l1, then n is the length of l2. Otherwise, n is the length of l1, cnt is the number of common prefix bits in the binary representation of the last x and y, and 2^cnt has been printed t times.

#Overall this is what the function does:This function reads a series of pairs of distinct non-negative integers from standard input, calculates the number of common prefix bits in their binary representations, and prints the result as a power of 2 for each pair. The function processes multiple pairs as specified by an initial integer input, and it handles pairs of varying bit lengths by padding the shorter binary representation with a leading zero if necessary.

