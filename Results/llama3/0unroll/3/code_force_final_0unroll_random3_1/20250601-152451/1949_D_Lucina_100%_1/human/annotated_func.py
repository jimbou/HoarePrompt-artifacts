#State of the program right berfore the function call: stdin contains n+1 inputs: the first input is an integer n (2 <= n <= 24), and the next n inputs are strings of length n, where each character is one of 'F', 'S', '?', or '.'.
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
        
    #State: Output State: n is an integer between 2 and 24, a is a list of n+1 integers, b is a list of n+1 integers, xx is a list containing n strings of length n with characters 'F', 'S', '?', or '.', stdin contains no inputs.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: sa contains the indices of the list a where the value is greater than 0 and the corresponding value in list b is 0, sb contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, n remains unchanged, a remains unchanged, b remains unchanged, xx remains unchanged, and stdin remains unchanged.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: The list `sa` now contains the indices of the list `a` where the value is greater than 0 and the corresponding value in list `b` is 0, plus the indices where both `a` and `b` are 0. The value of `t` is updated to the new length of `sa`. All other variables remain unchanged.
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
            
        #State: Output State: The loop has executed all iterations, and the variable `nx` has been updated with a new string value in each iteration. The string `nx` now contains the concatenated characters from the 2D list `xx` at indices `i` and `j-1`, where `i` ranges from 1 to `n` and `j` ranges from 1 to `n`. If the character at `xx[i][j-1]` is '?', it is replaced with 'F' if either `i` or `j` is in the first `n//4 - 1` indices of the list `sa`, and 'S' otherwise. The updated string `nx` is printed in each iteration. All other variables, including `sa`, `t`, `a`, and `b`, remain unchanged.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: sa contains the indices of the list a where the value is greater than 0 and the corresponding value in list b is 0, sb contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, n remains unchanged, a remains unchanged, b remains unchanged, xx remains unchanged, and stdin remains unchanged. The length of sa is less than the length of sb.
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
            
        #State: Output State: The loop iterates from 1 to n (inclusive), and for each iteration i, it constructs a new string nx. nx is constructed by iterating over the characters in the i-th row of the 2D list xx. If the character is not '?', it is appended to nx. If the character is '?' and either the current row i or column j is in the first n//4 - 1 indices of sb, 'S' is appended to nx; otherwise, 'F' is appended. The constructed string nx is then printed. The loop does not modify any variables outside of the loop body, so the output state is the same as the initial state, with the addition of the printed strings nx.
    #State: *sa contains the indices of the list a where the value is greater than 0 and the corresponding value in list b is 0, sb contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, n remains unchanged, a remains unchanged, b remains unchanged, xx remains unchanged, and stdin remains unchanged. If the length of sa is greater than or equal to the length of sb, the loop has executed all iterations, and the variable nx has been updated with a new string value in each iteration. The string nx now contains the concatenated characters from the 2D list xx at indices i and j-1, where i ranges from 1 to n and j ranges from 1 to n. If the character at xx[i][j-1] is '?', it is replaced with 'F' if either i or j is in the first n//4 - 1 indices of the list sa, and 'S' otherwise. The updated string nx is printed in each iteration. Otherwise, the loop iterates from 1 to n (inclusive), and for each iteration i, it constructs a new string nx. nx is constructed by iterating over the characters in the i-th row of the 2D list xx. If the character is not '?', it is appended to nx. If the character is '?' and either the current row i or column j is in the first n//4 - 1 indices of sb, 'S' is appended to nx; otherwise, 'F' is appended. The constructed string nx is then printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the processed output. It takes n+1 inputs, where n is an integer between 2 and 24, and the next n inputs are strings of length n containing characters 'F', 'S', '?', or '.'. The function then identifies indices where 'F' and 'S' characters are present, and replaces '?' characters in the strings based on certain conditions. If the number of 'F' indices is greater than or equal to the number of 'S' indices, it replaces '?' characters with 'F' or 'S' based on the presence of indices in the first n//4 - 1 indices of the 'F' list. Otherwise, it replaces '?' characters with 'S' or 'F' based on the presence of indices in the first n//4 - 1 indices of the 'S' list. Finally, it prints the processed strings.

