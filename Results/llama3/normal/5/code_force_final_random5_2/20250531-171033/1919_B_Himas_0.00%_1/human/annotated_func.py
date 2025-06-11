#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
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
        
    #State: `i` is equal to the number of test cases, `s` is an integer equal to the input value, `e` is an empty string, `P` is equal to the number of '+' characters in the original string `e` which is 0, `M` is equal to the number of characters that are not '+' in the original string `e` which is 0, the difference between the number of '+' characters and the number of characters that are not '+' in the original string `e` which is `P` - `M` = 0 has been printed, `q` is not defined, stdin is empty, and this is printed: 0

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a string of '+' and '-' characters. It then counts the number of '+' and '-' characters in the string and prints their difference. The function repeats this process for each test case until all input has been read.

