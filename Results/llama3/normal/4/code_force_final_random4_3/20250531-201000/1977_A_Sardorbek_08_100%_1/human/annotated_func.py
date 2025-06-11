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
        
    #State: a is equal to 0, i is equal to the initial value of a, b and c are integers, q is a tuple containing two integers, stdin is empty. If b equals c, 'YES' is printed a times. If b is less than c, 'NO' is printed a times. If b is greater than c, if b and c have the same parity, 'Yes' is printed a times. Otherwise, 'No' is printed a times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers. It then compares these integers and prints 'YES' if they are equal, 'NO' if the first integer is less than the second, 'Yes' if the first integer is greater than the second and they have the same parity, and 'No' otherwise. The function repeats this process for the specified number of test cases, leaving the input stream empty upon completion.

