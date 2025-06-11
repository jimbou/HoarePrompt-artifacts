#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500.
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: The number of alternating sequences of '0's and '1's in each string, minus 1 if the string starts with '0' and ends with '1', is printed to the console for each of the t strings. The value of t remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings consisting of '0' and '1' characters. It then calculates and prints the number of alternating sequences of '0's and '1's in each string, subtracting 1 if the string starts with '0' and ends with '1'. The function does not return any value but prints the results to the console, leaving the input variable t unchanged.

