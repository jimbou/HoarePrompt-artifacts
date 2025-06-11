#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
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
        
    #State: a is an integer between 0 and 99 (inclusive), i is a is an integer between 0 and 99 (inclusive), b is an integer between 1 and 100 (inclusive), c is an integer between 1 and 100 (inclusive), q is a tuple containing two integers between 1 and 100 (inclusive), stdin contains multiple lines of input, each containing two integers n and m (1 <= n, m <= 100), b and c are updated to the values of the two integers from the last line of stdin. If b is equal to c, 'YES' is printed. If b is less than c, 'NO' is printed. If b is greater than or equal to c, then if a and b have the same parity, 'Yes' is printed, otherwise 'No' is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and m. It then iterates through each line, comparing the values of n and m, and prints 'YES' if they are equal, 'NO' if n is less than m, 'Yes' if n is greater than or equal to m and n and t have the same parity, and 'No' otherwise. The function does not return any value, but modifies the state of the program by printing the results of the comparisons and updating the values of n and m to the last line of input.

