#State of the program right berfore the function call: stdin contains t+2t lines. The first line contains one integer t (1 <= t <= 1000). Each of the following t blocks of two lines contains an integer n (2 <= n <= 50) and a list of n space-separated integers (0 <= a_i <= 1) respectively.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `t` is at least 1000, `n` is an integer, `a` is a list of integers with all leading and trailing zeros removed, `i` is equal to the length of `a`, the list `a` with all trailing zeros removed is no longer being printed, and the number of zeros in `a` which is equal to `res` is being printed, and `stdin` contains no input, and the list `a` is being printed. If any element of `a` is 0, then `res` is increased by the number of zeros in `a`, and the number of zeros in `a` which is equal to `res` is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results. It expects the input to contain an integer t, followed by t blocks of two lines each. The first line of each block contains an integer n, and the second line contains a list of n space-separated integers. The function removes leading and trailing zeros from each list, counts the number of zeros in the modified list, and prints the modified list and the count of zeros. It repeats this process for each block of input. After processing all input, the function does not return any value, but the input is consumed, and the results are printed to the console.

