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
        
    #State: The loop will print 'YES' if b equals c, 'NO' if b is less than c, 'Yes' if b and c have the same parity, and 'No' otherwise, for each line in stdin. The value of a will remain unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines each containing two integers n and m. It then prints 'YES' if n equals m, 'NO' if n is less than m, 'Yes' if n and m have the same parity, and 'No' otherwise, for each line. The function does not return any value and does not modify the input values.

