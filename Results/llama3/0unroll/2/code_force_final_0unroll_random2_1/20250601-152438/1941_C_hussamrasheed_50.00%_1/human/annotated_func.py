#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: The loop has executed t times, and for each execution, it has read an integer n and a string s from stdin, counted the occurrences of 'map' and 'pie' in s, and printed the sum of these counts. The values of t, n, s, m, and p have been updated accordingly after each execution. The final state is that t has been decremented to 0, and the last values of n, s, m, and p are stored in memory.

#Overall this is what the function does:This function reads a specified number of test cases from standard input, where each test case consists of an integer and a string. It then counts the occurrences of the substrings 'map' and 'pie' in each string, and prints the sum of these counts for each test case. The function processes all test cases and does not return any value.

