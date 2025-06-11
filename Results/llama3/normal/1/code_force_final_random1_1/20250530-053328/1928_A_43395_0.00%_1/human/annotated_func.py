#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle.
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
        
    #State: `a` and `b` are integers, `i` is `t`, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers representing the size of a rectangle. It then determines whether the rectangle can be divided into two equal parts by a diagonal, and prints 'yes' if possible, 'no' otherwise. The function processes all test cases and leaves the input stream empty.

