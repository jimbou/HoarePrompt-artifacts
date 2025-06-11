#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (2 <= n <= 500) and then n-1 integers x_2,...,x_n (1 <= x_i <= 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The output state will be a sequence of n integers, where each integer is the sum of the corresponding integer in the input sequence and the previous integer in the output sequence, starting with 500. For example, if the input is "3 2 3 4", the output will be "500 502 505 509".

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n-1 integers. It then generates a sequence of n integers, where each integer is the sum of the corresponding integer in the input sequence and the previous integer in the output sequence, starting with 500. The function prints each generated sequence.

