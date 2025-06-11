#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (2 <= n <= 2 * 10^5 and n is even), then two strings of length n consisting of characters '<' and/or '>'.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: t is an integer greater than or equal to 0, _ is t, n is an integer between 2 and 2 * 10^5 inclusive and is even, a is a string of length n consisting of characters '<' and/or '>', b is a string of length n consisting of characters '<' and/or '>', stdin contains no test cases, i is n - 1. If for all i in range(1, n, 2), neither a[i] and b[i + 1] are both '<' nor a[i] and b[i - 1] are both '<', then 'yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an even integer n and two strings a and b of length n containing '<' and/or '>'. It then checks if there are any pairs of adjacent characters in a and b that are both '<'. If such a pair is found, it prints 'No'; otherwise, it prints 'yes'. The function processes all test cases and prints the result for each case.

