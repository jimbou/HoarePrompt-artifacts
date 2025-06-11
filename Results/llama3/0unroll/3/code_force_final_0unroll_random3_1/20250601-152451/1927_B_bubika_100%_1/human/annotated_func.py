#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: The string `a` remains unchanged, stdin is empty, and the standard output contains `t` lines, each representing a string of lowercase English letters.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. For each test case, it generates a string of lowercase English letters based on the input integers and prints the resulting string to standard output. The function processes multiple test cases and produces multiple output strings, one for each test case.

