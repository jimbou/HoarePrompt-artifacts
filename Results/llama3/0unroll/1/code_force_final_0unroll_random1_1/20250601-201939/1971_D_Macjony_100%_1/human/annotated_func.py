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
        
    #State: The output will be t lines, each containing an integer. The integer on each line represents the minimum number of segments of consecutive 1's or 0's in the corresponding input string s, with the exception that if a string starts with a 0 followed by a 1, the count is reduced by 1. The value of t remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings consisting of characters 0 and 1. It then processes each string, counting the minimum number of segments of consecutive 1's or 0's, with the exception that if a string starts with a 0 followed by a 1, the count is reduced by 1. The function prints the count for each string, resulting in t lines of output. The value of t remains unchanged.

