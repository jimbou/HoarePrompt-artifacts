#State of the program right berfore the function call: stdin contains n+1 inputs: first an integer n (2 <= n <= 24) and then n strings of length n. Each string contains only the characters F, S, ?, and .. The number of F and S characters in all strings is at most n/2 (rounded down). The i-th character of the j-th string and the j-th character of the i-th string are the same for all i and j.
    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    xx = ['']
    for i in range(1, n + 1):
        x = input()
        
        for j in range(1, n + 1):
            if x[j - 1] == 'F':
                a[i] += 1
                a[j] += 1
            elif x[j - 1] == 'S':
                b[i] += 1
                b[j] += 1
        
        xx.append(x)
        
    #State: `n` is an integer between 2 and 24 (inclusive), `a` is a list of `n+1` integers where the `i`-th and `j`-th elements are `n` if the character at index `j-1` of string `x` is 'F', otherwise `a` is a list of `n+1` zeros, `b` is a list of `n+1` integers where the values at indices 1 and 1 are both 1 and the rest are 0 if the character at index 0 of string `x` is 'S' and the character at index `j-1` of string `x` is not 'F', otherwise `b` is a list of `n+1` integers where `b[1]` is `n-1` and `b[j]` is 1 if the character at index `j-1` of string `x` is 'S', `xx` is a list containing `n+1` strings: an empty string and `n` strings `x`, `x` is a string of length `n`, `stdin` is empty, `i` is `n+1`, and `j` is `n+1`.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: n is an integer between 2 and 24 (inclusive), a is a list of n+1 integers where the i-th and j-th elements are n if the character at index j-1 of string x is 'F', otherwise a is a list of n+1 zeros, b is a list of n+1 integers where the values at indices 1 and 1 are both 1 and the rest are 0 if the character at index 0 of string x is 'S' and the character at index j-1 of string x is not 'F', otherwise b is a list of n+1 integers where b[1] is n-1 and b[j] is 1 if the character at index j-1 of string x is 'S', xx is a list containing n+1 strings: an empty string and n strings x, x is a string of length n, stdin is empty, i is n+1, j is n+1, sa is a list containing the values from 1 to n+1 where a[i] is greater than 0 and b[i] is 0, sb is a list containing the values from 1 to n+1 where b[i] is greater than 0 and a[i] is 0.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `n` is an integer between 2 and 24 (inclusive), `a` is a list of n+1 integers where the i-th and j-th elements are n if the character at index j-1 of string x is 'F', otherwise a is a list of n+1 zeros, `b` is a list of n+1 integers where the values at indices 1 and 1 are both 1 and the rest are 0 if the character at index 0 of string x is 'S' and the character at index j-1 of string x is not 'F', otherwise b is a list of n+1 integers where b[1] is n-1 and b[j] is 1 if the character at index j-1 of string x is 'S', `xx` is a list containing n+1 strings: an empty string and n strings x, `x` is a string of length n, `stdin` is empty, `i` is n+1, `j` is n+1, `sa` is a list containing the values from 1 to n+1 where a[i] is greater than 0 and b[i] is 0 and also contains the values of `i` from 1 to n+1 if a[i] is 0 and b[i] is 0, `sb` is a list containing the values from 1 to n+1 where b[i] is greater than 0 and a[i] is 0, `t` is the length of sa which is greater than or equal to the length of sb plus the number of times a[i] is 0 and b[i] is 0.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sa[:n // 4 - 1] or j in sa[:n // 4 - 1]:
                    nx += 'F'
                else:
                    nx += 'S'
            
            print(nx)
            
        #State: n is an integer between 2 and 24 (inclusive), a is a list of n+1 integers where the i-th and j-th elements are n if the character at index j-1 of string x is 'F', otherwise a is a list of n+1 zeros, b is a list of n+1 integers where the values at indices 1 and 1 are both 1 and the rest are 0 if the character at index 0 of string x is 'S' and the character at index j-1 of string x is not 'F', otherwise b is a list of n+1 integers where b[1] is n-1 and b[j] is 1 if the character at index j-1 of string x is 'S', xx is a list containing n+1 strings: an empty string and n strings x, x is a string of length n, stdin is empty, i is n+1, j is n+1, sa is a list containing the values from 1 to n+1 where a[i] is greater than 0 and b[i] is 0 and also contains the values of i from 1 to n+1 if a[i] is 0 and b[i] is 0, sb is a list containing the values from 1 to n+1 where b[i] is greater than 0 and a[i] is 0, t is the length of sa which is greater than or equal to the length of sb plus the number of times a[i] is 0 and b[i] is 0, nx is a string containing either the character at index j - 1 of string x if xx[i][j - 1] is not '?', otherwise nx is either 'F' or 'S'. If i or j is in the first n // 4 - 1 elements of sa, then nx is 'F', otherwise nx is 'S'. If xx[i][j - 1] is not '?', then nx is updated to nx plus the character at index j - 1 of string xx[i]. If xx[i][j - 1] is '?', then nx is appended with 'F' if i or j is in the first n // 4 - 1 elements of sa, otherwise nx is appended with 'S'. nx is now updated to nx plus the character at index j - 1 of string xx[i] if xx[i][j - 1] is not '?', otherwise nx is appended with 'F' if i or j is in the first n // 4 - 1 elements of sa, otherwise nx is appended with 'S', and nx is printed.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` is an integer between 2 and 24 (inclusive), `a` is a list of n+1 integers where the i-th and j-th elements are n if the character at index j-1 of string x is 'F', otherwise a is a list of n+1 zeros, `b` is a list of n+1 integers where the values at indices 1 and 1 are both 1 and the rest are 0 if the character at index 0 of string x is 'S' and the character at index j-1 of string x is not 'F', otherwise b is a list of n+1 integers where b[1] is n-1 and b[j] is 1 if the character at index j-1 of string x is 'S', `xx` is a list containing n+1 strings: an empty string and n strings x, `x` is a string of length n, `stdin` is empty, `i` is n+1, `j` is n+1, `sa` is a list containing the values from 1 to n+1 where a[i] is greater than 0 and b[i] is 0, `sb` is a list containing the values from 1 to n+1 where b[i] is greater than 0 and a[i] is 0, and the length of sa is less than the length of sb. If a[i] is 0 and b[i] is 0, then sb now contains the values from 1 to n+1.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sb[:n // 4 - 1] or j in sb[:n // 4 - 1]:
                    nx += 'S'
                else:
                    nx += 'F'
            
            print(nx)
            
        #State: nx is a string of length n, where each character is 'S' if the corresponding character in string x is 'S' and the index is in the first n // 4 - 1 elements of sb, otherwise 'F', and this string nx is being printed, and i is n+1, and j is n+1.
    #State: *n is an integer between 2 and 24 (inclusive), a is a list of n+1 integers where the i-th and j-th elements are n if the character at index j-1 of string x is 'F', otherwise a is a list of n+1 zeros, b is a list of n+1 integers where the values at indices 1 and 1 are both 1 and the rest are 0 if the character at index 0 of string x is 'S' and the character at index j-1 of string x is not 'F', otherwise b is a list of n+1 integers where b[1] is n-1 and b[j] is 1 if the character at index j-1 of string x is 'S', xx is a list containing n+1 strings: an empty string and n strings x, x is a string of length n, stdin is empty, i is n+1, j is n+1, sa is a list containing the values from 1 to n+1 where a[i] is greater than 0 and b[i] is 0 and also contains the values of i from 1 to n+1 if a[i] is 0 and b[i] is 0, sb is a list containing the values from 1 to n+1 where b[i] is greater than 0 and a[i] is 0, t is the length of sa which is greater than or equal to the length of sb plus the number of times a[i] is 0 and b[i] is 0, nx is a string containing either the character at index j - 1 of string x if xx[i][j - 1] is not '?', otherwise nx is either 'F' or 'S'. If i or j is in the first n // 4 - 1 elements of sa, then nx is 'F', otherwise nx is 'S'. If xx[i][j - 1] is not '?', then nx is updated to nx plus the character at index j - 1 of string xx[i]. If xx[i][j - 1] is '?', then nx is appended with 'F' if i or j is in the first n // 4 - 1 elements of sa, otherwise nx is appended with 'S'. nx is now updated to nx plus the character at index j - 1 of string xx[i] if xx[i][j - 1] is not '?', otherwise nx is appended with 'F' if i or j is in the first n // 4 - 1 elements of sa, otherwise nx is appended with 'S', and nx is printed if the length of sa is greater than or equal to the length of sb. Otherwise, nx is a string of length n, where each character is 'S' if the corresponding character in string x is 'S' and the index is in the first n // 4 - 1 elements of sb, otherwise 'F', and this string nx is being printed.

#Overall this is what the function does:This function reads input from the standard input, processes it, and prints the results. It first reads an integer n (2 <= n <= 24) and then n strings of length n, each containing only the characters F, S, ?, and .. The function then analyzes the input strings, identifies the characters at each position, and prints the processed strings. If the length of the list of indices where 'F' appears is greater than or equal to the length of the list of indices where 'S' appears, it replaces '?' with 'F' or 'S' based on the indices. Otherwise, it replaces '?' with 'S' or 'F' based on the indices. The function prints the processed strings.

