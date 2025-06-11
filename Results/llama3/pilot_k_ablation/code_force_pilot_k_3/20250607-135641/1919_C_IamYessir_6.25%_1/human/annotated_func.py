#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
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
        
    #State: `n` is an integer, `i` is `len(b) - 1`, `lit` is a list of integers, `cp` is 0, `a` is a list containing the first element of `lit` and all elements of `lit` that are greater than or equal to the last element of `a`, `b` is a list containing all elements of `lit` that are less than the last element of `a`, `s` is the number of pairs of consecutive elements in `a` where the second element is greater than the first, plus the number of pairs of consecutive elements in `b` where the second element is greater than the first, stdin contains no test cases, and the number of pairs of consecutive elements in `a` and `b` where the second element is greater than the first, which is `s`, is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then processes each test case by splitting the integers into two lists, a and b, based on whether each integer is greater than or equal to the last element of a. The function then counts the number of pairs of consecutive elements in both lists where the second element is greater than the first and prints this count. The function repeats this process for all test cases and does not return any value.

