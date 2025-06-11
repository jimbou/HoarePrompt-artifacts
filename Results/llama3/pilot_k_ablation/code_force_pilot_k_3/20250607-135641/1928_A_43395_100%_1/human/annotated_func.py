#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: `input` is a valid integer and is greater than or equal to 0, `i` is equal to the value of `input`, `a` and `b` are integers between 1 and 10^9 and are the values of the last line of stdin, stdin contains multiple lines of input, the first line has been read and the rest of the lines have been read and processed. If both `a` and `b` are even, then 'yes' is printed. Otherwise, if either `a` is even and half of `a` is not equal to `b`, or `b` is even and half of `b` is not equal to `a`, then 'yes' is printed. Otherwise, 'no' is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains a single integer t (1 <= t <= 10^4) and each subsequent line contains two integers a and b (1 <= a, b <= 10^9). It then checks each pair of integers (a, b) and prints 'yes' if both are even, or if one is even and half of it is not equal to the other. Otherwise, it prints 'no'. The function processes all input lines and prints the corresponding results.

