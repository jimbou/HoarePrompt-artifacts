#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500 (inclusive).
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: The number of strings in stdin is reduced to 0, and the console contains t number of lines, each containing a number between 1 and 501 (inclusive).

#Overall this is what the function does:Reads a specified number of binary strings from standard input, counts the number of times a '1' is followed by a '0' in each string, and prints the count plus one for each string.

