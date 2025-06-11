#State of the program right berfore the function call: stdin contains n+1 inputs: the first input is an integer n (2 <= n <= 24), and the next n inputs are strings of length n, where each character is either 'F', 'S', or '?'.
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
        
    #State: Output State: n is an integer between 2 and 24, a is a list of n+1 integers, where each integer represents the total number of 'F' characters in the input strings that correspond to the index of the integer, b is a list of n+1 integers, where each integer represents the total number of 'S' characters in the input strings that correspond to the index of the integer, xx is a list containing n strings, where each string is an input string of length n, stdin is empty.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: The loop has iterated over the range from 1 to n (inclusive), and for each iteration, it has checked the conditions for the current index i. If the condition a[i] > 0 and b[i] == 0 is true, it has appended the value of i to the list sa. If the condition b[i] > 0 and a[i] == 0 is true, it has appended the value of i to the list sb. The loop has not modified the values of n, a, b, xx, or stdin.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: The loop has iterated over the range from 1 to n (inclusive), and for each iteration, it has checked the conditions for the current index i. If the condition a[i] == 0 and b[i] == 0 is true, it has appended the value of i to the list sa. The loop has not modified the values of n, a, b, xx, or stdin. The current value of the length of sa is greater than or equal to the length of sb plus the number of iterations where a[i] == 0 and b[i] == 0.
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
            
        #State: Output State: The loop has iterated over the range from 1 to n (inclusive), and for each iteration, it has checked the conditions for the current index i. If the condition a[i] == 0 and b[i] == 0 is true, it has appended the value of i to the list sa. The loop has not modified the values of n, a, b, xx, or stdin. The current value of the length of sa is greater than or equal to the length of sb plus the number of iterations where a[i] == 0 and b[i] == 0.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: The loop has iterated over the range from 1 to n (inclusive), and for each iteration, it has checked the conditions for the current index i. If the condition a[i] == 0 and b[i] == 0 is true, it has appended the value of i to the list sb. The loop has not modified the values of n, a, b, xx, or stdin. Additionally, the length of list sb is greater than the length of list sa.
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
            
        #State: Output State: The loop has iterated over the range from 1 to n (inclusive), and for each iteration, it has constructed a string nx by iterating over the range from 1 to n (inclusive). For each character in the string xx[i][j - 1], if the character is not '?', it has been appended to nx. If the character is '?' and either i or j is in the first n // 4 elements of list sb, 'S' has been appended to nx; otherwise, 'F' has been appended to nx. After constructing nx, it has been printed. The values of n, a, b, xx, stdin, sb, and sa remain unchanged.
    #State: The program has iterated over the range from 1 to n (inclusive) and checked conditions for each index i. If the length of list sa is greater than or equal to the length of list sb, the program has appended indices i to sa where a[i] == 0 and b[i] == 0, without modifying n, a, b, xx, or stdin. If the length of sa is less than the length of sb, the program has constructed a string nx by iterating over xx and replacing '?' with 'S' or 'F' based on the presence of i or j in the first n // 4 elements of list sb, and then printed nx, leaving n, a, b, xx, stdin, sb, and sa unchanged.

#Overall this is what the function does:This function reads n+1 inputs from stdin, where n is an integer between 2 and 24, and the next n inputs are strings of length n containing 'F', 'S', or '?' characters. It then processes these inputs to determine the presence of 'F' and 'S' characters in each string and their corresponding indices. Based on the counts of 'F' and 'S' characters, it constructs new strings by replacing '?' characters with 'F' or 'S' according to certain rules. Finally, it prints the constructed strings. The function does not return any value, and its output is the printed strings.

