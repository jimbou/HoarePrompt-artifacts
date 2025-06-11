#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: a is an integer greater than or equal to 0 and less than or equal to 100, i is a-1, b is an integer between 1 and 100 inclusive, c is an integer between 1 and 100 inclusive, q is a tuple containing b and c, stdin is empty. If b is equal to c, 'YES' is printed. If b is not equal to c, then if b is less than c, 'NO' is printed. If b and c have the same parity, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers. It then checks the parity of the two integers and prints 'YES' if they are equal, 'NO' if the first integer is less than the second, 'Yes' if they have the same parity, and 'No' otherwise. The function processes all test cases and prints the corresponding results.

