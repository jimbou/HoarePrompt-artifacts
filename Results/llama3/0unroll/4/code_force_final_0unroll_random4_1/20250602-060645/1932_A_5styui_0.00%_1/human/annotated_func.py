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
        
    #State: The value of s is 0, and the value of a is t-1. The loop has executed t-1 times, and for each execution, it has printed the count of '@' characters in the input string. The input string has been processed and the count of '@' characters has been printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters in each string and prints the count for each test case. The function iterates through all test cases, processing each string and printing the '@' character count, before resetting the count for the next test case.

