#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters, where each character is either '.', '@', or '*'.
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: a is an integer between 1 and 1000 inclusive, s is 0, stdin contains t-a test cases, i is a-1, d is an integer, b is a string, j is equal to the length of string b.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters in each string and prints the count. The function repeats this process for each test case, and after processing all test cases, it leaves the input stream with the remaining test cases (if any). The function does not modify the input variables, and its primary purpose is to count and print the occurrences of '@' characters in each test case string.

