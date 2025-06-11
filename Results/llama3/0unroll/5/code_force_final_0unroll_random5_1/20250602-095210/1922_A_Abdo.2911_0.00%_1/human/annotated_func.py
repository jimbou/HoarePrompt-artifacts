#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        template = []
        
        for i in range(n):
            if a[i] == b[i]:
                template.append(a[i])
            else:
                template.append(a[i].upper())
        
        match_a_b = True
        
        for i in range(n):
            if template[i].islower():
                if a[i] != template[i] or b[i] != template[i]:
                    match_a_b = False
                    break
            elif a[i].lower() == template[i].lower() or b[i].lower() == template[i
                ].lower():
                match_a_b = False
                break
        
        match_c = True
        
        for i in range(n):
            if template[i].islower():
                if c[i] != template[i]:
                    match_c = False
                    break
            elif c[i].lower() == template[i].lower():
                match_c = False
                break
        
        if match_a_b and not match_c:
            print('YES')
        else:
            print('NO')
        
    #State: The output state is a sequence of 'YES' or 'NO' for each test case, indicating whether the conditions are met or not. The value of `t` remains unchanged, and the input test cases are consumed. The output is printed to the console, and the program terminates.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and three strings a, b, and c, each of length n. It then checks if the strings a and b can be transformed into a common template by making some characters in a or b uppercase, and if the resulting template matches string c except for the uppercase characters. If the conditions are met, it prints 'YES' for that test case; otherwise, it prints 'NO'. The function processes all test cases and prints the results to the console, leaving the input state unchanged.

