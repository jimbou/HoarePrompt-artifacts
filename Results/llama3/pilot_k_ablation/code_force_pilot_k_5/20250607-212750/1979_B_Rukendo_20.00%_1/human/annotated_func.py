#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated non-negative integers x and y such that x != y. The number of test cases is specified in the first line of stdin.
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
        
    #State: t is 0, stdin contains no test cases, x is 0, y is 0, x != y is false, l1 and l2 are lists containing the binary representation of the last x and y respectively, n is the length of l1 which is equal to the length of l2, i is n, cnt is the number of equal elements from the start of l1 and l2, and 2 to the power of cnt has been printed for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two distinct non-negative integers. For each test case, it converts the integers to binary, compares them from the most significant bit, and prints the number of equal bits from the start (2 to the power of the number of equal bits). The function processes all test cases and then terminates, leaving the input stream empty.

