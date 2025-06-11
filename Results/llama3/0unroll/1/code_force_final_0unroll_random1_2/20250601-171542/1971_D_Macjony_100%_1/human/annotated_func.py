#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters 0 and 1.
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
        
    #State: The output state is a list of integers, where each integer represents the number of alternating sequences of 0s and 1s in the corresponding input string, minus 1 if the string starts with 0 and ends with 1. The input strings and the value of t remain unchanged.

#Overall this is what the function does:This function reads a series of binary strings from standard input and outputs the number of alternating sequences of 0s and 1s in each string, with a special case where if a string starts with 0 and ends with 1, it decrements the count by 1. The function processes multiple strings as specified by an initial integer input, and the input strings and the count of strings remain unchanged.

