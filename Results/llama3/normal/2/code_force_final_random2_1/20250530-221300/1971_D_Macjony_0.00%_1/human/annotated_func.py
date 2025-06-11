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
        
    #State: `t` is an integer between 1 and 500 inclusive, stdin is empty, `i` is equal to `t`, `s` is a string consisting of characters '0' and '1' with length between 1 and 500, `j` is equal to `len(s) - 1`. If there exists at least one pair of adjacent characters in `s` where the first character is '0' and the second character is '1', then `count` is equal to the number of pairs of adjacent characters in `s` that are different minus 1. Otherwise, `count` is equal to the number of pairs of adjacent characters in `s` that are different. The value of `count` is being printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, where the number of strings is specified by an integer at the beginning of the input. For each string, it counts the number of pairs of adjacent characters that are different, but if there is at least one pair where '0' is followed by '1', it decrements this count by 1. The function then prints the resulting count for each string.

