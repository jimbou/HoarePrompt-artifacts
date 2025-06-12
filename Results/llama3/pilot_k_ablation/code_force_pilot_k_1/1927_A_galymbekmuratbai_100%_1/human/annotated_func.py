#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a positive integer, and each subsequent pair of lines contains a positive integer and a string consisting of 'W' and 'B' characters.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: t is 0, n is the last integer read from stdin, s is the last string read from stdin, first_black is the index of the first 'B' in the last string, last_black is the index of the last 'B' in the last string, min_paint is the minimum paint required for the last string which is last_black - first_black + 1, and the minimum paint required for each string has been printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains a positive integer t, and each subsequent pair of lines contains a positive integer n and a string s consisting of 'W' and 'B' characters. It calculates the minimum number of paint required to paint the 'B' characters in each string, which is the difference between the indices of the first and last 'B' characters plus one. The function then prints the minimum paint required for each string. After processing all input, the function leaves the program state with t being 0, n and s being the last integer and string read from stdin, and the minimum paint required for each string printed.

