#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
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
        
    #State: a is an integer between 1 and 100 (inclusive), i is a-1, b is an integer between 1 and 100 inclusive, c is an integer between 1 and 100 inclusive, q is a tuple containing two integers between 1 and 100 inclusive, stdin is empty. If b is equal to c, 'YES' is printed. If b is not equal to c, then if b is less than c, 'NO' is printed. If b is greater than or equal to c, then if a and b have the same parity, 'Yes' is printed, otherwise 'No' is printed.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and m. It then prints 'YES' if n equals m, 'NO' if n is less than m, and either 'Yes' or 'No' depending on whether t and n have the same parity if n is greater than or equal to m. The function processes t pairs of integers and prints a result for each pair.

