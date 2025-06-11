#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of three lines: the first line contains an integer n, the second line contains a string s of n characters, and the third line contains a string f of n characters. The characters in s and f are either '0' or '1'.
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: n is an integer greater than or equal to 0, s is a string of n characters, t is a string of n characters, a is equal to the number of characters in s that are greater than the corresponding characters in t, b is equal to the number of characters in s that are less than the corresponding characters in t, i is n, stdin contains 0 test cases, and the maximum of a and b is being printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the maximum difference between the number of characters in two strings that are greater than or less than each other. It accepts no parameters and returns no value, but instead prints the result for each test case. The function's purpose is to compare characters in pairs of strings and output the maximum difference in the number of greater or lesser characters.

