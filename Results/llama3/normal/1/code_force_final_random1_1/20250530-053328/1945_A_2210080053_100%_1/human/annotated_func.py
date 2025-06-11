#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers a, b, c (0 <= a, b, c <= 10^9).
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: a is an integer equal to the first integer in the t-th line, b is an integer equal to the sum of the second and third integers in the t-th line, c is an integer equal to the third integer in the t-th line, stdin contains no lines of input, open(0) is a file object with no lines, s is the t-th line, and this is printed: (a - -b // 3, -1)[c < b % 3].

#Overall this is what the function does:The function reads multiple lines of input from standard input, where the first line contains a single integer t, and each of the following t lines contains three integers a, b, and c. It then processes each line, adding b and c, and prints either the result of a minus the integer division of the sum of b and c by 3, or -1, depending on whether c is less than the remainder of the sum of b and c divided by 3. After processing all lines, the function leaves the standard input empty and the file object open(0) with no lines.

