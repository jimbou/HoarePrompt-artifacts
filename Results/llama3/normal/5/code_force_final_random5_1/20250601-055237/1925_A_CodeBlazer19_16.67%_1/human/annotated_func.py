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
        
    #State: `t` is at least 1, `i` is `t`, `n` is an integer between 1 and 26 inclusive, `k` is an integer between 1 and 26 inclusive, `s` is a string containing `k` characters from 'a' to the character represented by the ASCII value `k+96`, `stdin` is empty, `j` is `k+96`. If `k` is 1, the string 'a' repeated `n` times is printed. If `k` is greater than 1, either `s` or `2*s` is printed, depending on the value of `n`.

#Overall this is what the function does:The function reads input from stdin, expecting a specific format: the first line contains an integer t, followed by t lines, each containing two integers n and k. It then generates a string s consisting of k characters from 'a' to the character represented by the ASCII value k+96. Depending on the value of k, it prints either the string 'a' repeated n times (if k is 1) or either s or 2*s (if k is greater than 1), with the choice between s and 2*s depending on the value of n. After processing all input lines, stdin is left empty.

