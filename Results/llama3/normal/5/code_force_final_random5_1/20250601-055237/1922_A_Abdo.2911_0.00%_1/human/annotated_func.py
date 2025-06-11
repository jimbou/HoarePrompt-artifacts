#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each of length n consisting of lowercase Latin letters.
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
        
    #State: t is equal to 0, n is an integer greater than or equal to 0, a is a string, b is a string, c is a string, i is equal to n, template is a list containing characters from string a (or b) if a[i] is equal to b[i], otherwise template is a list containing the uppercase of the characters from string a. If match_a_b is True and match_c is False, 'YES' is printed. Otherwise, either match_a_b is False or match_c is True, and 'NO' is printed. stdin contains 0 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings a, b, and c. It compares the strings a and b character by character, creating a template string where matching characters are copied as is, and non-matching characters are converted to uppercase. It then checks if string c matches the template string, allowing uppercase characters in c to match either the uppercase or lowercase version in the template. If string c does not match the template, but strings a and b do, the function prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and then terminates.

