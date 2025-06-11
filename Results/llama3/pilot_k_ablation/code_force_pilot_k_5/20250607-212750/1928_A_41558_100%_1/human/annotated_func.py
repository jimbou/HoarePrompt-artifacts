#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: `n` is greater than or equal to 0, `i` is `n`, `a` and `b` are integers that are assigned values from the input, stdin is empty. If both `a` and `b` are odd, then 'NO' is printed. If either `a` is twice `b` and `b` is odd or `b` is twice `a` and `a` is odd, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains a single integer t (1 <= t <= 10^4) and each of the following t lines contains two integers a and b (1 <= a, b <= 10^9). It then checks each pair of integers a and b to determine if they meet certain conditions. If both a and b are odd, or if either a is twice b and b is odd or b is twice a and a is odd, it prints 'NO'. Otherwise, it prints 'YES'. The function continues this process until all input lines have been processed, at which point stdin is empty.

