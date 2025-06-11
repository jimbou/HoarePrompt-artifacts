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
        
    #State: `t` is 0, `x` is 0, `y` is 0, `l1` is a list containing the binary representation of the original value of `x`, `l2` is a list containing the binary representation of the original value of `y`, `_` is `t-1`, `n` is the length of `l1` if the length of `l2` is less than the length of `l1`, otherwise `n` is the length of `l2`, `i` is `n-1`, `cnt` is equal to the number of matching elements at the beginning of `l1` and `l2`, stdin contains 0 lines of input, and 2 raised to the power of the number of matching elements at the beginning of `l1` and `l2` has been printed for each iteration of the loop.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains a single integer t representing the number of test cases, and each subsequent line contains two distinct non-negative integers x and y. For each test case, it converts x and y into binary representation, compares the binary representations from left to right, and prints 2 raised to the power of the number of matching elements at the beginning of the binary representations. The function does not return any value but prints the results for each test case.

