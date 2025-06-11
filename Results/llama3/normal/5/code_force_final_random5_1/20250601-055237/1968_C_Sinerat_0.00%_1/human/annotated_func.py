#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 500) and then n-1 space-separated integers x_2, ..., x_n (1 <= x_i <= 500). The sum of values n over all test cases does not exceed 2 * 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: `n` is a positive integer, `i` is `n`, `x` is a list of integers, `a` is a list of `n` integers where the first element is 500 and the rest are the cumulative sum of 500 and the elements of `x`, stdin contains multiple test cases minus `n` inputs: an integer and a list of integers, and the list `a` is being printed, where the first element of `a` is 500 and the rest are the cumulative sum of 500 and the elements of `x`.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n-1 integers. It then generates a list of n integers, where the first element is 500 and the rest are the cumulative sum of 500 and the elements of the input list. Finally, it prints the generated list.

