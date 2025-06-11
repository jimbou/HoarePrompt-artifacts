#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: `i` is `t`, `a` and `b` are integers (1 <= a, b <= 10^9), stdin contains multiple lines of input. The first line contains a single integer 0 (0 <= 0 <= 10^4). Each of the following 0 lines contains two integers a and b (1 <= a, b <= 10^9). If both `a` and `b` are even, 'yes' is printed. Otherwise, if either `a` equals `-b` or `b` equals `-a`, 'no' is printed. If the difference between `a` and `b` is odd, 'yes' is printed. Otherwise, 'no' is printed.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, representing the number of test cases, and each subsequent line contains two integers a and b. It then iterates through each test case, checking the parity of a and b, and prints 'yes' if both are even or their difference is odd, and 'no' if either a equals -b or b equals -a, or if the difference between a and b is even. The function effectively determines whether the sum of a and b is even or odd for each test case and prints the corresponding result.

