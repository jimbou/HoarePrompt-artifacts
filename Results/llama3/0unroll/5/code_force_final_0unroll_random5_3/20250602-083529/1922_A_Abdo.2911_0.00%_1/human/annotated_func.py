#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case. The number of 'YES' or 'NO' printed will be equal to the value of t. The output will indicate whether the strings a and b match the template and string c does not match the template for each test case.

#Overall this is what the function does:The function reads input from the standard input, processes it, and prints a series of 'YES' or 'NO' to the console. It accepts no parameters and returns no value. The function's purpose is to determine whether, for each test case, strings 'a' and 'b' match a generated template and string 'c' does not match the template. The final state of the program is that the console contains a series of 'YES' or 'NO' outputs, one for each test case, indicating whether the condition was met for each case.

