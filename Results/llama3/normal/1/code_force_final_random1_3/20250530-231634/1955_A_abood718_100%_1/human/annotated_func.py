#State of the program right berfore the function call: stdin contains t+1 lines, where t is a positive integer. The first line contains t. Each of the following t lines contains three positive integers n, a, and b, such that 1 <= n <= 100, 1 <= a <= 30, and 1 <= b <= 30.
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: `i` is equal to `t`, stdin is empty.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains the number of subsequent lines (t), and each subsequent line contains three positive integers (n, a, b). It then processes each line, applying different calculations based on the values of a and b, and prints the result for each line. The function continues until all input lines have been processed, at which point stdin is empty and the function concludes.

