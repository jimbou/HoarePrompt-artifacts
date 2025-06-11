#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (n), then two strings of length n consisting of '<' and '>' characters. n is even and 2 <= n <= 2 * 10^5. The total length of all strings over all test cases doesn't exceed 2 * 10^5.
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
        
    #State: The loop will execute t times, each time reading three inputs from stdin: an integer n and two strings a and b of length n. It will then check if there are any pairs of adjacent characters in a and b that are both '<'. If such a pair is found, it will print 'No' and move on to the next test case. If no such pair is found after checking all pairs, it will print 'yes'. The total length of all strings over all test cases will not exceed 2 * 10^5.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two strings a and b of length n. It checks if there are any pairs of adjacent characters in a and b that are both '<'. If such a pair is found, it prints 'No' and moves on to the next test case. If no such pair is found after checking all pairs, it prints 'yes'. The function processes all test cases and prints the result for each case.

