#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= len(s) <= 500) consisting of characters '0' and '1'.
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        flag = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) != int(s[i + 1]):
                count += 1
            if int(s[i]) < int(s[i + 1]):
                flag = 1
        
        if flag == 0:
            print(count + 1)
        else:
            print(count)
        
    #State: t is 0, q is t, stdin contains 0 strings s, s is a string of length between 1 and 500 consisting of characters '0' and '1', i is len(s) - 1. If flag is 0, the value of count + 1 is being printed, where count + 1 is between 1 and len(s). If flag is 1, count (where count is between 0 and len(s) - 1) is being printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, where the number of strings is specified by an initial integer. For each string, it counts the number of transitions from 0 to 1 or 1 to 0 and prints the total number of transitions plus one if the string is non-increasing, otherwise it prints the total number of transitions. The function processes all input strings and does not return any value.

