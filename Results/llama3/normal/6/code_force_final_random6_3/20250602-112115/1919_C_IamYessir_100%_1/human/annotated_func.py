#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 ≤ n ≤ 2⋅10^5) and then a list of n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [], []
        
        cp = 0
        
        for i in range(0, n):
            if len(a) == 0:
                x = float('inf')
            else:
                x = a[-1]
            if len(b) == 0:
                y = float('inf')
            else:
                y = b[-1]
            if x > y:
                if y >= lit[i]:
                    b.append(lit[i])
                elif lit[i] > x:
                    b.append(lit[i])
                elif x >= lit[i] and lit[i] > y:
                    a.append(lit[i])
            elif x == y:
                a.append(lit[i])
            elif x < y:
                if x >= lit[i]:
                    a.append(lit[i])
                elif lit[i] > y:
                    a.append(lit[i])
                elif y >= lit[i] and lit[i] > x:
                    b.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: `n` is an integer greater than or equal to 0, `lit` is a list of integers, `cp` is 0, `_` is equal to the number of test cases, `a` is a list of integers, `i` is equal to `len(b)`, `x` is the last element of list `a`, `b` is a non-empty list, `y` is the last element of list `b`. `s` is equal to the number of pairs of consecutive elements in `b` where the second element is greater than the first element, plus `len(a) - 1` if the first element of `a` is greater than the second element of `a`, or `len(a) - 2` otherwise, and the value of `s` is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes the list of integers, splitting it into two lists a and b based on certain conditions. The function counts the number of pairs of consecutive elements in both lists where the second element is greater than the first element and prints this count. The function repeats this process for each test case.

