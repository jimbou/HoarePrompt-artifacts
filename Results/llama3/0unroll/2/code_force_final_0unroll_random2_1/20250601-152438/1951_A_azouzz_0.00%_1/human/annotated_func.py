#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer t (1 <= t <= 1000). The second line contains a binary string s of size n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: The loop will execute 't' number of times, and for each iteration, it will print either 'YES' or 'NO' based on the conditions in the loop body. The output will be a series of 'YES' or 'NO' printed to the console, one for each test case. The value of 't' will remain unchanged, and the stdin will be empty after all test cases have been processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then analyzes the binary string and prints 'YES' or 'NO' to the console based on the following conditions: if the count of '1's is greater than 2 and even, it prints 'YES'; if the count of '1's is greater than 2 and odd, or if the count is 1, it prints 'NO'; if the string contains '11', it prints 'NO'; otherwise, it prints 'YES'. The function processes all test cases and prints the corresponding results, leaving the standard input empty.

