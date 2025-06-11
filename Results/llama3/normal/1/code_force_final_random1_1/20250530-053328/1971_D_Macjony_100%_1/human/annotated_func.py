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
        
    #State: t is equal to 0, i is equal to the initial value of t, stdin is empty, s is unchanged, j is equal to len(s) - 1, and count is equal to the number of pairs of adjacent characters in s that are different minus 1 if there exists a pair of adjacent characters in s where the first character is '0' and the second character is '1', otherwise count is equal to the number of pairs of adjacent characters in s that are different.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of pairs of adjacent characters that are different in each string, and prints the count. If a string contains a pair of adjacent characters where the first character is '0' and the second character is '1', the count is decremented by 1. The function processes multiple strings, as specified by an initial integer input, and leaves the input strings unchanged.

