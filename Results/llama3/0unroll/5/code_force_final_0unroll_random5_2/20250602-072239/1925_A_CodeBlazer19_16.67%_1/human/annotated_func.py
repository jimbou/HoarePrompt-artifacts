#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 676). Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: Output State: `t` is an integer between 1 and 676 (inclusive), stdin contains no lines of input (end of file), and the standard output contains `t` lines of output, each line containing a string of characters.

#Overall this is what the function does:The function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and k. It then generates a string s consisting of k lowercase alphabets starting from 'a' and prints t lines of output, each containing the string s repeated n times if k is 1, or repeated twice if n is not 1 and k is not 1, resulting in t lines of output in the standard output.

