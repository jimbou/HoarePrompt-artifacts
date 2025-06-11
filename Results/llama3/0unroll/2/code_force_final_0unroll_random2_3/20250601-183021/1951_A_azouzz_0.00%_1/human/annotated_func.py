#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 ≤ t ≤ 1000) and then a binary string of size n (1 ≤ n ≤ 50).
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
        
    #State: The loop will have printed 'YES' or 'NO' for each test case, indicating whether the binary string contains a certain pattern, and the value of `t` will be unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then checks the binary string for specific patterns and prints 'YES' or 'NO' for each test case, indicating whether the string contains the pattern. The function does not modify the input values and only prints the results for each test case.

