#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
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
        
    #State: `n` is 0, `lit` is an empty list, `cp` is 0, `a` is a list of integers, `b` is a list of integers with at least `len(a)` + `len(b)` - 1 elements, `x` is the last element of list `a`, `y` is the last element of list `b`, `i` is `len(b)`, `s` is the number of pairs of adjacent elements in `a` where the second element is greater than the first plus the number of pairs of adjacent elements in `b` where the second element is greater than the first, and stdin contains no more test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then processes these integers, splitting them into two lists a and b based on certain conditions. The function counts the number of pairs of adjacent elements in both lists where the second element is greater than the first and prints this count. The function repeats this process for all test cases in the input.

