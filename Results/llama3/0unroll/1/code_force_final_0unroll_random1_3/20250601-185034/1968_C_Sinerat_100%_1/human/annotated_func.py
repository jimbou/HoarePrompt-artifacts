#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a single integer t (1\le t\le 10^4), then for each test case, the first line contains a single integer n (2\le n\le 500) and the second line contains n-1 integers x_2,\dots,x_n (1\le x_i\le 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The output state will be the values of a for each test case, where a is a list of n integers. The first element of a will always be 1000, and each subsequent element will be the sum of the previous element and the corresponding value from the input list x.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n-1 integers. It then generates a new list a of length n, where the first element is always 1000, and each subsequent element is the sum of the previous element and the corresponding value from the input list. The function prints the generated list a for each test case.

