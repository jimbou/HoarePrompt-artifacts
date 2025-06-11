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
        
    #State: The loop will execute 'a' number of times, where 'a' is an integer between 1 and 100 inclusive. In each iteration, it will read two integers 'b' and 'c' from the standard input, and print 'YES' if 'b' is equal to 'c', 'NO' if 'b' is less than 'c', 'Yes' if 'b' and 'c' have the same parity (i.e., both are even or both are odd), and 'No' otherwise. The state of 'a' remains unchanged after the loop execution.

#Overall this is what the function does:This function reads an integer 't' from the standard input, representing the number of test cases. For each test case, it reads two integers 'n' and 'm', and prints 'YES' if 'n' equals 'm', 'NO' if 'n' is less than 'm', 'Yes' if 'n' and 'm' have the same parity, and 'No' otherwise. The function does not return any value and does not modify the input variables.

