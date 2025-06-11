#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters '0' and '1'.
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: t is at least 1, q is t-1, stdin is empty, s is a string consisting of characters '0' and '1' with length between 1 and 500, i is len(s) - 1, count is the number of times a character in s is greater than the next character, and the value of count + 1 is being printed, which is the number of times a character in s is greater than the next character plus 1

#Overall this is what the function does:This function reads a series of binary strings from standard input, where the number of strings is specified by an initial integer. For each string, it counts the number of times a character is greater than the next character and prints this count plus one. The function processes all input strings and prints the results before concluding, leaving the standard input empty.

