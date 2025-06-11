#State of the program right berfore the function call: stdin contains n+1 inputs: first an integer n (2 <= n <= 24) and then n strings of length n. Each string contains only the characters 'F', 'S', '?', and '.'. The i-th character of the j-th string and the j-th character of the i-th string are the same for all i and j. At most n//2 characters in the input are 'F' or 'S'.
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
        
    #State: n is an integer between 2 and 24, a is a list of n+1 integers, b is a list of n+1 integers, xx is a list containing n strings of length n, stdin is empty.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: The loop iterates from 1 to n (inclusive), checking each index i in lists a and b. If a[i] is greater than 0 and b[i] is 0, it appends i to list sa. If b[i] is greater than 0 and a[i] is 0, it appends i to list sb. After the loop finishes, the state of the variables is as follows:
    #
    #- n remains unchanged, still an integer between 2 and 24.
    #- a remains unchanged, still a list of n+1 integers.
    #- b remains unchanged, still a list of n+1 integers.
    #- xx remains unchanged, still a list containing n strings of length n.
    #- sa is now a list containing indices i where a[i] > 0 and b[i] == 0.
    #- sb is now a list containing indices i where b[i] > 0 and a[i] == 0.
    #- stdin remains empty.
    #
    #Note that the exact values in sa and sb depend on the initial values of a and b, which are not specified.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: sa contains all indices i where a[i] == 0 and b[i] == 0, in addition to the indices i where a[i] > 0 and b[i] == 0. The length of sa is greater than or equal to the length of sb.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sa[:n // 4] or j in sa[:n // 4]:
                    nx += 'F'
                else:
                    nx += 'S'
            
            print(nx)
            
        #State: The output state after the loop executes all the iterations is a series of strings, each representing a row in the 2D array xx. The strings are constructed by iterating over each character in the corresponding row of xx. If the character is not '?', it is added to the string as is. If the character is '?' and the current row index i or column index j is in the first n//4 indices of sa, the string is appended with 'F'. Otherwise, the string is appended with 'S'. The resulting strings are printed to the console.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: *n is an integer between 2 and 24. a is a list of n+1 integers. b is a list of n+1 integers. xx is a list containing n strings of length n. sa is a list containing indices i where a[i] > 0 and b[i] == 0. sb is a list containing indices i where b[i] > 0 or (a[i] == 0 and b[i] == 0). The length of sa is less than or equal to the length of sb. stdin is empty.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sb[:n // 4] or j in sb[:n // 4]:
                    nx += 'S'
                else:
                    nx += 'F'
            
            print(nx)
            
        #State: The loop prints n strings of length n. Each string is constructed by iterating over the characters in the corresponding string in xx. If the character is not '?', it is added to the new string. If the character is '?' and either the row or column index is in the first n/4 elements of sb, 'S' is added to the new string. Otherwise, 'F' is added to the new string. The values of n, a, b, sa, and sb remain unchanged.
    #State: The program prints a series of strings, each representing a row in the 2D array xx. If the length of sa is greater than or equal to the length of sb, the strings are constructed by iterating over each character in the corresponding row of xx. If the character is not '?', it is added to the string as is. If the character is '?' and the current row index i or column index j is in the first n//4 indices of sa, the string is appended with 'F'. Otherwise, the string is appended with 'S'. If the length of sa is less than the length of sb, the strings are constructed by iterating over the characters in the corresponding string in xx. If the character is not '?', it is added to the new string. If the character is '?' and either the row or column index is in the first n/4 elements of sb, 'S' is added to the new string. Otherwise, 'F' is added to the new string. The values of n, a, b, sa, and sb remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints a series of strings to the console. It first reads an integer n and n strings of length n, then counts the occurrences of 'F' and 'S' in each string and stores them in lists a and b. It then identifies indices where 'F' or 'S' appears exclusively and stores them in lists sa and sb. Depending on the lengths of sa and sb, it constructs new strings by replacing '?' characters with 'F' or 'S' based on the indices in sa or sb, and prints these strings to the console.

