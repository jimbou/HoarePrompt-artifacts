#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 676) followed by t lines, each containing two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
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
        
    #State: The output will be `t` lines, each containing a string of lowercase English letters. The string on each line will be `k` characters long, and will consist of the first `k` lowercase English letters (i.e., 'a' through the `k`-th letter of the alphabet). If `k` is 1, the string will be repeated `n` times. If `k` is greater than 1, the string will be repeated twice, unless `n` is 1, in which case it will be repeated only once.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines, each containing two integers n and k. It then generates a string of the first k lowercase English letters and prints it t times. If k is 1, the string is repeated n times; otherwise, it is repeated twice unless n is 1, in which case it is repeated only once. The output consists of t lines, each containing a string of k characters.

