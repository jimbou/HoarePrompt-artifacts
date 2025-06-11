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
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: The output state will be a series of integers, each representing the number of alternating sequences of 0s and 1s in the corresponding input string, with a correction applied if a sequence starts with 0 and ends with 1. The number of output integers will be equal to the value of `t`. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings consisting of 0s and 1s. It then calculates the number of alternating sequences of 0s and 1s in each string, applying a correction if a sequence starts with 0 and ends with 1. The function prints the corrected count of alternating sequences for each input string, with the total number of output integers equal to the value of t.

