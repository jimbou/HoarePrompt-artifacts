#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each of length n, consisting of lowercase Latin letters.
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
        
    #State: The loop has finished executing, and the output state is determined by the values of `match_a_b` and `match_c` after the last iteration. If `match_a_b` is True and `match_c` is False, then 'YES' is printed. Otherwise, either `match_a_b` is False or `match_c` is True, and 'NO' is printed. The values of `match_a_b` and `match_c` are determined based on the values of `template[i]`, `a[i]`, `b[i]`, and `c[i]` for each iteration of the loop.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case. It takes no parameters and returns no values. The function's purpose is to determine whether a given string c matches a template created from strings a and b, with specific matching rules. The final state of the program is the output of 'YES' or 'NO' for each test case, indicating whether the string c matches the template.

