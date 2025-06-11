#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: `n` is an integer greater than or equal to 0, `l` is a list of integers, `a` and `b` are the two smallest elements in `l`, `c` is the number of elements in `l` that are greater than `b`, `stdin` contains no test cases, and `x` is `n-1`. The value of `c` is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then finds the two smallest elements in the list and counts the number of elements greater than the second smallest element. The function prints the count for each test case.

