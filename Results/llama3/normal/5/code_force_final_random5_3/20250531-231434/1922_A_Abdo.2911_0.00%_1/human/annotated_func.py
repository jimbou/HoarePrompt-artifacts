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
        
    #State: `t` is an integer between 0 and 1000 (inclusive), `_` is `t`, `n` is an integer greater than or equal to 0, `a` is a string, `b` is a string, `c` is a string, `i` is `n`, either 'YES' or 'NO' has been printed `t` times, and stdin is empty. If `match_a_b` is True and `match_c` is False, then 'YES' is printed. Otherwise, either `match_a_b` is False or `match_c` is True, and 'NO' is printed. In both cases, if `template[i]` is lowercase, then `match_a_b` and `match_c` remain unchanged if `c[i]` is equal to `template[i]`, otherwise `match_a_b` is False and `match_c` is False. If `template[i]` is uppercase, then `match_a_b` is False if any of the following conditions are met: `template[i]` is lowercase and `a[i]` is not equal to `template[i]` or `b[i]` is not equal to `template[i]`; `template[i]` is uppercase and `a[i]` is equal to `template[i]` (ignoring case) or `b[i]` is equal to `template[i]` (ignoring case); `template[i]` is uppercase and `a[i].lower()` is equal to `template[i].lower()` or `b[i].lower()` is equal to `template[i].lower()`; `a[i]` is not equal to `template[i]` or `b[i]` is not equal to `template[i]`; `a[i].lower()` is equal to `template[i].lower()` or `b[i].lower()` is equal to `template[i].lower()`. Otherwise, `match_a_b` remains unchanged. `match_c` is False if `c[i]` is not equal to `template[i]` (ignoring case), otherwise `match_c` is True. `template` is a list containing the characters at indices 0 through `n-1` of string `a` if the characters at those indices in `a` and `b` are equal, or the uppercase characters at those indices in string `a` if the characters at those indices in `a` and `b` are not equal.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints 'YES' or 'NO' based on certain conditions. It accepts an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters. The function creates a template by comparing characters in strings a and b, and then checks if the template matches strings a, b, and c. If the template matches a and b but not c, it prints 'YES'; otherwise, it prints 'NO'. The function repeats this process t times and then exits, leaving stdin empty.

