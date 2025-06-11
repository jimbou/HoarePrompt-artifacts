#State of the program right berfore the function call: stdin contains a number of test cases t (1 <= t <= 10^4), followed by t test cases. Each test case contains an integer n (2 <= n <= 500) followed by n-1 integers x_2, ..., x_n (1 <= x_i <= 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: n is at least n, i is n-1, x is a list of n integers, a is a list of n integers with the first element being 500 and the rest being the cumulative sum of x, stdin contains 0 test cases, _ is t-1, and the list a is being printed, and the list a which is [500, cumulative sum of x[0], cumulative sum of x[0] + x[1], cumulative sum of x[0] + x[1] + x[2], ... , cumulative sum of x[0] + x[1] + x[2] + ... + x[n-1]] is being printed

#Overall this is what the function does:The function reads a number of test cases from standard input, where each test case consists of an integer n followed by n-1 integers. It then generates a list of n integers, where the first element is 500 and the rest are the cumulative sum of the input integers. Finally, it prints the generated list for each test case.

