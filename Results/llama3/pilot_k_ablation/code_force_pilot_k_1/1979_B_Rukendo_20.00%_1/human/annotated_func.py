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
        
    #State: `t` is 0, stdin is empty, `_` is `t`, `x` is 0, `y` is 0, `l1` is an empty list, `l2` is an empty list, `n` is 0, `cnt` is 0, `i` is 0.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t representing the number of test cases, and each subsequent line contains two space-separated integers x and y. For each test case, it compares the binary representations of x and y from right to left and counts the number of matching bits. It then prints the result as a power of 2 to the console. After processing all test cases, the function leaves the input stream empty and the variables x, y, and other temporary variables in a zero or empty state.

