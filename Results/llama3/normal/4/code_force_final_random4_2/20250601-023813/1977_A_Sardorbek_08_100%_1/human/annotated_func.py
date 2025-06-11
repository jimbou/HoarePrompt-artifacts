#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
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
        
    #State: a is between 1 and 100 (inclusive), i is a-1, b and c are integers between 1 and 100, q is a tuple containing two integers between 1 and 100, stdin contains multiple lines of input, each containing two integers n and m (1 <= n, m <= 100), with a less lines than initially. If b is equal to c, 'YES' is printed. If b is less than c, 'NO' is printed. If b is greater than c, 'Yes' is printed if b and c have the same parity, otherwise 'No' is printed.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t (1 <= t <= 100) and each subsequent line contains two integers n and m (1 <= n, m <= 100). It then iterates over these input lines, comparing the values of n and m. If n is equal to m, it prints 'YES'. If n is less than m, it prints 'NO'. If n is greater than m, it checks if n and m have the same parity (i.e., both are even or both are odd) and prints 'Yes' if they do, or 'No' if they don't. The function does not return any value, but instead prints the results directly to the console.

