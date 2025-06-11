#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 500). The second line contains n-1 integers (1 <= x_i <= 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: n is an integer equal to the input value, x is a list of integers from the input, a is a list of length n with the first element being 500 and the rest being the cumulative sum of 500 and the elements of x, i is n-1, _ is any value, stdin is empty, and the list a is being printed. The list a contains the first element 500 and the rest are the cumulative sum of 500 and the elements of x.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and a list of n-1 integers. It then generates a new list a of length n, where the first element is 500 and the remaining elements are the cumulative sum of 500 and the elements of the input list. Finally, it prints the list a. The function processes multiple test cases and prints the corresponding lists a for each case.

