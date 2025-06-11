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
        
    #State: The output state is a series of 'YES', 'NO', 'Yes', or 'No' printed to the console, depending on the values of b and c read from stdin, and the value of a. The number of lines printed is equal to the value of a. The values of a, b, and c are not changed. The stdin contains t-1 lines, each containing two integers n and m (1 <= n, m <= 100).

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, and prints 'YES' or 'NO' to the console based on the values of the integers and the parity of the test case number. The function does not modify the input values or return any value, but instead prints the results directly to the console.

