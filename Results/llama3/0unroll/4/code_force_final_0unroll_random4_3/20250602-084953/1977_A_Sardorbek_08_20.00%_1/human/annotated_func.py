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
        
    #State: Output State: The loop will execute 'a' times, each time reading a line from stdin, parsing it into two integers 'b' and 'c', and printing 'YES' if 'b' equals 'c', 'NO' if 'b' is less than 'c', 'Yes' if 'a' and 'b' have the same parity, and 'No' otherwise. The value of 'a' remains unchanged.

#Overall this is what the function does:This function reads an integer 't' from standard input, representing the number of test cases, and then for each test case, it reads two integers 'n' and 'm'. It then checks the conditions: if 'n' equals 'm', it prints 'YES'; if 'n' is less than 'm', it prints 'NO'; if 't' and 'n' have the same parity (both odd or both even), it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but prints the results for each test case.

