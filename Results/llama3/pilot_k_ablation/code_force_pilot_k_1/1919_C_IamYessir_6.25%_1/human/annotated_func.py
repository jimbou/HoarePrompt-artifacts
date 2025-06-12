#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 ≤ n ≤ 2*10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: `stdin` is empty, `_` is the number of test cases, `n` is 0, `lit` is an empty list, `a` and `b` are empty lists, `cp` is 0, `s` is the sum of the number of pairs of consecutive integers in all test cases where the second integer is greater than the first.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then processes each list to identify pairs of consecutive integers where the second integer is greater than the first, and counts the total number of such pairs across all test cases. The function returns the total count of such pairs, leaving the input stream empty and all variables in a reset state.

