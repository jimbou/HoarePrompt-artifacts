#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the string) and then a string consisting of "+" and "-" characters.
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(P - M)
        
    #State: i is the number of test cases in stdin minus one, s is an integer, stdin contains no test cases, e is an empty string, P is the number of '+' characters in the original string e, M is the number of '-' characters in the original string e, and the difference between the number of '+' characters and the number of '-' characters in the original string e is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer (the length of the string) and a string containing "+" and "-" characters. It then calculates and prints the difference between the number of "+" characters and the number of "-" characters in each string. After processing all test cases, the function leaves the standard input empty.

