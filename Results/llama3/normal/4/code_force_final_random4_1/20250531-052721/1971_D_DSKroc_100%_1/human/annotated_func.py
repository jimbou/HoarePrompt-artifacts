#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with a length between 1 and 500.
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
        
    #State: t is an integer between 1 and 500 inclusive, q is t-1, s is a string consisting of characters '0' and '1' with a length between 1 and 500, stdin contains 0 strings, i is len(s) - 1, count is the number of times a '0' is followed by a '1' in s. If a '0' is not followed by a '1' in s, then count + 1 is printed. Otherwise, the number of times a '0' is followed by a '1' in s, which is count, is printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input and prints the number of times a '0' is followed by a '1' in each string. If a string does not contain a '0' followed by a '1', it prints the total number of transitions from '0' to '1' plus one. The function processes multiple strings, with the number of strings specified by an integer read from standard input before the strings.

