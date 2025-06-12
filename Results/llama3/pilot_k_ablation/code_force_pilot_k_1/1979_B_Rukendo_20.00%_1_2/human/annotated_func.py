#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two space-separated integers x and y (0 <= x, y <= 10^9, x != y).
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
        
    #State: t is an integer between 1 and 10^4 (inclusive), stdin contains 0 lines of input, _ is t-1, x is 0, y is 0, l1 is a list containing the binary representation of the last value of x, l2 is a list containing the binary representation of the last value of y in reverse order, n is equal to the length of l1, cnt is the number of common prefix bits between the binary representations of the last x and y, and 2 raised to the power of cnt for each pair of x and y has been printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates the number of common prefix bits in their binary representations, and prints the result as a power of 2 for each pair. It processes multiple pairs as specified by an initial count read from standard input.

