#State of the program right berfore the function call: stdin contains n+1 inputs: the first input is an integer n (2 <= n <= 24), and the next n inputs are strings of length n, each string containing characters '.', 'F', 'S', or '?'. The number of 'F' and 'S' characters in all strings is at most n/2 (rounded down). The i-th character of the j-th string and the j-th character of the i-th string are the same for all i and j.
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
        
    #State: n is an integer between 2 and 24 (inclusive), a is a list of n+1 integers, b is a list of n+1 integers, xx is a list containing n strings of length n, each string containing characters '.', 'F', 'S', or '?', stdin is empty.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: sa contains the indices of the list a where the value is greater than 0 and the corresponding value in list b is 0, sb contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, n is an integer between 2 and 24 (inclusive), a is a list of n+1 integers, b is a list of n+1 integers, xx is a list containing n strings of length n, each string containing characters '.', 'F', 'S', or '?', stdin is empty.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: The value of sa is updated to contain the indices of the list a where the value is greater than 0 and the corresponding value in list b is 0, plus the indices of the list a where both a and b are 0. The value of sb remains unchanged. The value of n, a, b, xx, stdin, and t remain unchanged.
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
            
        #State: Output State: The value of nx is updated to contain the string of characters that are not '?' in the corresponding row of the 2D list xx, and 'F' or 'S' based on the conditions in the loop. The value of i and j are updated to n + 1. The values of sa, sb, n, a, b, xx, stdin, and t remain unchanged.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: The output state is the same as the initial state, with the exception that sb now contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, as well as the indices where both a and b are 0.
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
            
        #State: Output State: The output state is the same as the initial state, with the exception that sb now contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, as well as the indices where both a and b are 0.
    #State: *The output state is updated based on the comparison of the lengths of lists sa and sb. If the length of sa is greater than or equal to the length of sb, the value of nx is updated to contain the string of characters that are not '?' in the corresponding row of the 2D list xx, and 'F' or 'S' based on the conditions in the loop, and the values of i and j are updated to n + 1. The values of sa, sb, n, a, b, xx, stdin, and t remain unchanged. If the length of sa is less than the length of sb, the output state remains the same as the initial state, with the exception that sb now contains the indices of the list b where the value is greater than 0 and the corresponding value in list a is 0, as well as the indices where both a and b are 0.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts n+1 inputs, where n is an integer between 2 and 24, and the next n inputs are strings of length n containing characters '.', 'F', 'S', or '?'. The function then analyzes the input strings, identifies patterns, and prints the updated strings with '?' characters replaced based on the identified patterns. The function performs the following actions:

