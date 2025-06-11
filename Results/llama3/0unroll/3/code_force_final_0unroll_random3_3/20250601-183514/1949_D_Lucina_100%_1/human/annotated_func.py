#State of the program right berfore the function call: stdin contains n+1 inputs: first an integer n (2 <= n <= 24) and then n strings of length n. Each string contains only the characters F, S, ?, and .. The number of F and S characters across all strings is at most n/2 (rounded down). The i-th character of the j-th string and the j-th character of the i-th string are the same for all i and j.
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
        
    #State: n is an integer between 2 and 24, a is a list of n+1 integers, b is a list of n+1 integers, xx is a list containing n strings of length n. Each string contains only the characters F, S, ?, and .. The number of F and S characters across all strings is at most n/2 (rounded down). The i-th character of the j-th string and the j-th character of the i-th string are the same for all i and j.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: The lists sa and sb are populated with indices of a and b, respectively. The indices in sa correspond to elements in a that are greater than 0 and have a corresponding element in b that is 0. The indices in sb correspond to elements in b that are greater than 0 and have a corresponding element in a that is 0. The other variables (n, a, b, and xx) remain unchanged.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: The length of list sa is assigned to variable t, the lists sa and sb are populated with indices of a and b, respectively. The indices in sa correspond to elements in a that are greater than 0 and have a corresponding element in b that is 0, or elements in both a and b that are 0. The indices in sb correspond to elements in b that are greater than 0 and have a corresponding element in a that is 0. The other variables (n, a, b, and xx) remain unchanged. The current value of the length of sa is greater than or equal to the length of sb.
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
            
        #State: The loop has executed n times, printing a string of length n for each iteration. The string nx is constructed by iterating over the elements of the 2D list xx. If an element is not '?', it is appended to nx. If the current row or column index is in the first n // 4 - 1 elements of sa, 'F' is appended to nx; otherwise, 'S' is appended. The values of n, a, b, sa, sb, and xx remain unchanged.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: *The lists sa and sb are populated with indices of a and b, respectively. The indices in sa correspond to elements in a that are greater than 0 and have a corresponding element in b that is 0. The indices in sb correspond to elements in b that are greater than 0 and have a corresponding element in a that is 0, or both a and b are 0. The other variables (n, a, b, and xx) remain unchanged. The length of sa is less than or equal to the length of sb.*
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
            
        #State: The variable nx is populated with a string of 'S' and 'F' characters. The string nx is printed n times, each time with a different set of 'S' and 'F' characters. The other variables (n, a, b, sa, sb, and xx) remain unchanged.
    #State: *The lists sa and sb are populated with indices of a and b, respectively. The indices in sa correspond to elements in a that are greater than 0 and have a corresponding element in b that is 0. The indices in sb correspond to elements in b that are greater than 0 and have a corresponding element in a that is 0. The other variables (n, a, b, and xx) remain unchanged. If the length of sa is greater than or equal to the length of sb, then the loop has executed n times, printing a string of length n for each iteration. The string nx is constructed by iterating over the elements of the 2D list xx. If an element is not '?', it is appended to nx. If the current row or column index is in the first n // 4 - 1 elements of sa, 'F' is appended to nx; otherwise, 'S' is appended. The values of n, a, b, sa, sb, and xx remain unchanged. If the length of sa is less than the length of sb, then the variable nx is populated with a string of 'S' and 'F' characters. The string nx is printed n times, each time with a different set of 'S' and 'F' characters. The other variables (n, a, b, sa, sb, and xx) remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts n+1 inputs: an integer n (2 <= n <= 24) and n strings of length n, each containing only the characters F, S, ?, and .. The function then populates two lists, sa and sb, with indices of a and b, respectively, based on certain conditions. Depending on the length of sa and sb, it either prints n strings of length n, where each string is constructed by iterating over the elements of the 2D list xx and appending 'F' or 'S' based on the current row or column index, or it prints n strings of length n, where each string is populated with 'S' and 'F' characters. The function does not return any value.

