#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500.
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: The output state will contain t integers, each representing the number of "peaks" in the corresponding input string. A "peak" is defined as a position in the string where the current character is greater than the next character. The count of peaks for each string is incremented by 1 before being printed. The input strings themselves remain unchanged.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of "peaks" in each string (where a peak is a position where the current character is greater than the next), increments the count by 1, and prints the result for each string. The input strings remain unchanged.

