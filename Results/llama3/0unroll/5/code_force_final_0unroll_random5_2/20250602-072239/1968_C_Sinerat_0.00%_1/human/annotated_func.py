#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 integers x_2, ..., x_n (1 <= x_i <= 500). The number of test cases does not exceed 10^4.
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The output will be a sequence of numbers where each number is the sum of the previous number and the corresponding input number. The first number in each sequence will be 500. For example, if the input is 3 1 2, the output will be 500 501 503. If the input is 4 1 2 3, the output will be 500 501 503 506.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains an integer n, and the second line contains n-1 integers. It then generates a sequence of numbers, starting with 500, where each subsequent number is the sum of the previous number and the corresponding input number. The function prints each generated sequence.

