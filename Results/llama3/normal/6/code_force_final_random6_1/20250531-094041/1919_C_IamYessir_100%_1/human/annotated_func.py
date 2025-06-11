#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. The integer is a positive integer and does not exceed 2 * 10^5. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `n` is 0, `i` is equal to the length of `b`, `lit` is a list of integers, `cp` is 0, `b` is a list of integers, `a` is a list of integers, `s` is the number of times `a[i]` is greater than `a[i - 1]` for all `i` in the range from 1 to the length of `a` plus the number of times `b[i]` is greater than `b[i - 1]` for all `i` in the range from 1 to the length of `b`, and the value of `s` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n integers. It then processes the list of integers, splitting it into two lists a and b based on certain conditions. The function counts the number of times an element in list a is greater than its previous element, and the number of times an element in list b is greater than its previous element. Finally, it prints the total count of these occurrences for each test case.

