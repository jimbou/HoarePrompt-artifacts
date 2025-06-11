#State of the program right berfore the function call: stdin contains t+2*t lines. The first line contains one integer t (1 <= t <= 1000). Each of the following t lines contains one integer n (2 <= n <= 50). Each of the following t lines contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: The loop will print the number of zeros in the middle of each sequence of integers (excluding leading and trailing zeros) for each of the t sequences, and the value of t remains unchanged.

#Overall this is what the function does:The function reads input from stdin, processes t sequences of integers, and prints the number of zeros in the middle of each sequence (excluding leading and trailing zeros). The function does not modify the input value t.

