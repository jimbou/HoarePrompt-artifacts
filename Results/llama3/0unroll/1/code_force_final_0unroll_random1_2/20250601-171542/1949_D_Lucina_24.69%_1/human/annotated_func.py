#State of the program right berfore the function call: stdin contains n+1 inputs: the first input is an integer n (2 <= n <= 24), and the next n inputs are strings of length n, where each character is either 'F', 'S', '?', or '.'.
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
        
    #State: Output State: n is an integer between 2 and 24, a is a list of n+1 integers, where each integer represents the total number of 'F' characters in the input strings that correspond to the index of the integer, b is a list of n+1 integers, where each integer represents the total number of 'S' characters in the input strings that correspond to the index of the integer, xx is a list containing n strings, where each string is one of the input strings, stdin is empty.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: n is an integer between 2 and 24, a is a list of n+1 integers, where each integer represents the total number of 'F' characters in the input strings that correspond to the index of the integer, b is a list of n+1 integers, where each integer represents the total number of 'S' characters in the input strings that correspond to the index of the integer, xx is a list containing n strings, where each string is one of the input strings, sa is a list containing the indices of the input strings that contain only 'F' characters, sb is a list containing the indices of the input strings that contain only 'S' characters, stdin is empty.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: The list sa contains the indices of all the input strings that contain only 'F' characters or are empty strings, while the other variables remain unchanged.
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
            
        #State: Output State: The list sa contains the indices of all the input strings that contain only 'F' characters or are empty strings, while the other variables remain unchanged.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: *n is an integer between 2 and 24, a is a list of n+1 integers, where each integer represents the total number of 'F' characters in the input strings that correspond to the index of the integer, b is a list of n+1 integers, where each integer represents the total number of 'S' characters in the input strings that correspond to the index of the integer, xx is a list containing n strings, where each string is one of the input strings, sa is a list containing the indices of the input strings that contain only 'F' characters, sb is a list containing the indices of the input strings that contain only 'S' characters and the indices of the input strings that contain neither 'F' nor 'S' characters, stdin is empty. The number of indices of input strings that contain only 'S' characters is larger than the number of indices of input strings that contain only 'F' characters
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
            
        #State: The loop has executed n times, and for each iteration, a new string nx has been created and printed. The string nx is created by iterating over the characters of the string xx[i] and replacing '?' with 'S' if the index i or j is in the list sb[:n // 4], and 'F' otherwise. The lists a, b, xx, sa, sb, and stdin remain unchanged.
    #State: *n is an integer between 2 and 24, a is a list of n+1 integers, where each integer represents the total number of 'F' characters in the input strings that correspond to the index of the integer, b is a list of n+1 integers, where each integer represents the total number of 'S' characters in the input strings that correspond to the index of the integer, xx is a list containing n strings, where each string is one of the input strings, sa is a list containing the indices of the input strings that contain only 'F' characters or are empty strings, sb is a list containing the indices of the input strings that contain only 'S' characters, stdin is empty. If the number of strings with only 'F' characters is greater than or equal to the number of strings with only 'S' characters, the list sa contains the indices of all the input strings that contain only 'F' characters or are empty strings, while the other variables remain unchanged. Otherwise, the loop has executed n times, and for each iteration, a new string nx has been created and printed. The string nx is created by iterating over the characters of the string xx[i] and replacing '?' with 'S' if the index i or j is in the list sb[:n // 4], and 'F' otherwise. The lists a, b, xx, sa, sb, and stdin remain unchanged.

#Overall this is what the function does:This function reads n+1 inputs from stdin, where n is an integer between 2 and 24, and the next n inputs are strings of length n. It then analyzes these strings to determine the indices of strings that contain only 'F' characters, only 'S' characters, or neither. If the number of strings with only 'F' characters is greater than or equal to the number of strings with only 'S' characters, it prints the input strings with '?' characters replaced by 'F' if the string index or column index is in the list of 'F' indices, and 'S' otherwise. Otherwise, it prints the input strings with '?' characters replaced by 'S' if the string index or column index is in the list of 'S' indices, and 'F' otherwise.

