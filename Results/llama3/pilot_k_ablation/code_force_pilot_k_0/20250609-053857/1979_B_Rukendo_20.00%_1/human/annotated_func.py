#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers x and y (0 <= x, y <= 10^9, x != y). The number of test cases is given on the first line.
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
        
    #State: The output will be the number of times the binary representations of x and y are the same from right to left, multiplied by 2 to the power of that number, for each test case. The value of t will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two space-separated integers x and y. It then compares the binary representations of x and y from right to left and prints the number of matching bits multiplied by 2 to the power of that number, for each test case. The function does not modify the input values or the number of test cases.

