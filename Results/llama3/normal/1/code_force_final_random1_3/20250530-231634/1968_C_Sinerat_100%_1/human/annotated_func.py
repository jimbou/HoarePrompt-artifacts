#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 integers x_2,...,x_n (1 <= x_i <= 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: n is an integer, i is n, x is a list of integers, a is a list of n integers where the first element is 1000 and each subsequent element a[i] is the sum of 1000 and the cumulative sum of the elements in x up to index i-1, stdin contains no more test cases, and the list a is printed, where the first element of a is 1000 and each subsequent element a[i] is the sum of 1000 and the cumulative sum of the elements in x up to index i-1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n-1 integers. It then generates a list of n integers, where the first element is 1000 and each subsequent element is the cumulative sum of 1000 and the previous elements in the input list. Finally, it prints the generated list for each test case.

