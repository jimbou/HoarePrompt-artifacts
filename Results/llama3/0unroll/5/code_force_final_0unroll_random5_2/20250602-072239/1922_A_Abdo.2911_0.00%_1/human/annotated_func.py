#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case. The output will indicate whether the conditions specified in the code are met for each test case. The value of 't' will remain unchanged, and the input strings 'a', 'b', and 'c' will also remain unchanged. The loop will iterate 't' times, and for each iteration, it will read a new set of inputs for 'n', 'a', 'b', and 'c'. The output will be a series of 'YES' or 'NO' values, one for each test case, indicating whether the conditions are met for that test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings a, b, and c. It then checks if the conditions specified in the code are met for each test case. If the conditions are met, it prints 'YES' to the console; otherwise, it prints 'NO'. The function iterates over the test cases 't' times, where 't' is an integer read from standard input at the beginning. The input strings 'a', 'b', and 'c' remain unchanged throughout the process.

