#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings s (1 <= |s| <= 500) consisting of characters '0' and '1'.
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: t is an integer between 1 and 500 inclusive, q is t-1, stdin is empty, s is a string consisting of characters '0' and '1' with a length between 1 and 500 inclusive, i is len(s) - 1, and count is the number of times a character in s is greater than the next character in s, and the count of such occurrences plus one has been printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of times a character in each string is greater than the next character, and prints the count plus one for each string. The function processes a specified number of strings, which is also read from standard input.

