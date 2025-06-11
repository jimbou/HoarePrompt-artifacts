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
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: The output state will contain t integers, each representing the number of alternating sequences of '0' and '1' in the corresponding input string, with a correction applied if the string starts with '0' and ends with '1'.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of alternating sequences of '0' and '1' in each string, and prints the corrected count for each string. The correction is applied if the string starts with '0' and ends with '1'. The function processes multiple strings based on the initial input integer t, which specifies the number of strings to process.

