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
        
    #State: `t` is an integer between 0 and 500 inclusive, `i` is equal to `t`, stdin is empty, `s` is the last string read from stdin, `count` is the number of transitions from '0' to '1' or '1' to '0' in `s` plus 1, `j` is equal to `len(s) - 1`. If there is at least one transition from '0' to '1' in `s`, then `flag` is True and `count` is decreased by one. Otherwise, `flag` is False.

#Overall this is what the function does:This function reads a series of binary strings from standard input and prints the number of transitions between '0' and '1' in each string, adjusting the count if a transition from '0' to '1' occurs. It processes a specified number of strings, then terminates, leaving the input stream empty.

