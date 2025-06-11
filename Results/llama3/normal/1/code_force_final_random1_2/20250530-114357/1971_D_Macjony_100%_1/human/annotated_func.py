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
        
    #State: t is equal to 0, i is equal to t, stdin is empty, s is undefined, count is undefined, j is undefined, and flag is undefined.

#Overall this is what the function does:The function reads a series of binary strings from standard input, where the number of strings is specified by an integer t at the beginning. For each string, it counts the number of alternating sequences of '0's and '1's, adjusting the count if a sequence starts with '0' and ends with '1'. The function then prints the adjusted count for each string, effectively processing and transforming the input strings into their respective sequence counts.

