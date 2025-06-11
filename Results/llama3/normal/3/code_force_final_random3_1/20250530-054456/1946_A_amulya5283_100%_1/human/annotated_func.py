#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input())
    while t > 0:
        t -= 1
        
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        if n == 1:
            print(1)
        else:
            res = 0
            mdx = n // 2 + n % 2 - 1
            for i in range(mdx, n):
                if a[mdx] == a[i]:
                    res += 1
            print(res)
        
    #State: t is 0, stdin contains no test cases. If n is 1, 1 is printed for each test case with n equal to 1. If n is not 1, the number of times a[mdx] is equal to a[i] for i in range(mdx, n) is printed for each test case with n not equal to 1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then sorts the integers and, for each test case, prints the number of times the middle element (or the element just after the middle if n is even) appears in the second half of the sorted list. If n is 1, it simply prints 1. The function continues this process until all test cases have been read from standard input.

