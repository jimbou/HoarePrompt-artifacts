#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters 0 and 1, where the length of each string is between 1 and 500 (inclusive).
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: t is an integer between 1 and 500 (inclusive) and is equal to 0, q is t-1, stdin contains 0 strings, each consisting of characters 0 and 1, where the length of each string is between 1 and 500 (inclusive), s is a string consisting of characters 0 and 1, where the length of the string is between 1 and 500 (inclusive), count is the number of times a character in s is greater than the next character, i is the last index of s, and the value of count + 1 is being printed.

#Overall this is what the function does:This function reads a series of binary strings from standard input, where the number of strings is specified by an initial integer value. For each binary string, it counts the number of times a character is greater than the next character and prints the count plus one. The function processes all input strings and does not return any value, only printing the results for each string.

