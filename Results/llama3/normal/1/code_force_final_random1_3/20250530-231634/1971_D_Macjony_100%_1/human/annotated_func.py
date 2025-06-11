#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500 (inclusive).
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
        
    #State: t is greater than or equal to 0, i is t, stdin is empty, s is a string consisting of characters '0' and '1' with length between 1 and 500 (inclusive), if '0' is followed by '1' in s, then count is one less than the number of times '0' and '1' appear consecutively in s, otherwise count remains the same, and j is len(s) - 1, and the count is printed

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of consecutive '0' and '1' pairs in each string, and prints the count. If a '0' is followed by a '1' in a string, it decrements the count by 1. The function processes multiple strings as specified by the initial integer input, and it empties the standard input buffer in the process.

