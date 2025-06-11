#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: `_` is the number of test cases, `n` is an integer greater than or equal to 0, `l` is a list of integers, `x` is `n`, `a` is the smallest element in list `l`, `b` is the second smallest element in list `l` if it exists, otherwise `b` is infinity, and `c` is the number of elements in list `l` that are greater than `b`, and the number of elements in list `l` that are greater than `b` which is `c` is being printed, and stdin contains no more test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds the smallest and second smallest elements in each list, and counts the number of elements greater than the second smallest element. The function prints this count for each test case.

