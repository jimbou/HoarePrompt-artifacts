#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t strings, each consisting of characters '0' and '1' with length between 1 and 500 (inclusive).
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
        
    #State: The loop has iterated over all strings in stdin, and the count of changes in each string has been printed. The value of t is 0, and stdin is empty. The values of i and s are undefined. The value of count is between 0 and 500 (inclusive), and the value of flag is either True or False. The value of j is equal to the second last index of the last string in stdin.

#Overall this is what the function does:This function reads a series of binary strings from standard input, counts the number of changes between consecutive characters in each string, and prints these counts. It processes all input strings and leaves the input stream empty.

