#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500 (inclusive).
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
        
    #State: t is greater than or equal to 0, q is equal to t, stdin is empty, s is a string consisting of characters '0' and '1' with length between 1 and 500 (inclusive), i is equal to the length of s minus 1, count is equal to the number of times a '0' is followed by a '1' in s. If a '0' is not followed by a '1' in s, the number of times a '0' is followed by a '1' in s plus one is printed, which is equal to count + 1. If a '0' is followed by a '1' in s, the count of times a '0' is followed by a '1' in s which is equal to count is being printed.

#Overall this is what the function does:The function reads a series of binary strings from standard input, where each string consists of characters '0' and '1' with a length between 1 and 500 (inclusive). For each string, it counts the number of times a '0' is followed by a '1' and prints this count. If a string does not contain a '0' followed by a '1', it prints the count plus one. The function processes all input strings and then terminates, leaving the standard input empty.

