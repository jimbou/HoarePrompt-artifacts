#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: a is an integer between 1 and 100 inclusive, i is a-1, b is an integer between 1 and 100 inclusive, c is an integer between 1 and 100 inclusive, q is a tuple containing two integers between 1 and 100 inclusive, stdin contains 0 lines. If b is equal to c, 'YES' is printed. If b is not equal to c, then if b is less than c, 'NO' is printed. Otherwise, if a and b have the same parity, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines, each containing two integers n and m. It then checks each pair of integers and prints 'YES' if they are equal, 'NO' if the first integer is less than the second, or 'YES' if the first integer and the total number of pairs have the same parity, and 'NO' otherwise. The function consumes all input lines and does not return any value.

