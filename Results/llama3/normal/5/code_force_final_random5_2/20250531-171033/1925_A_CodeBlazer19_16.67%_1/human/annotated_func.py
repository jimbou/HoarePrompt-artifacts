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
        
    #State: `t` is an integer between 1 and 676 (inclusive), `i` is `t-1`, `n` is an integer between 1 and 26 (inclusive), `k` is an integer between 1 and 26 (inclusive) and greater than 0, `s` is a string containing `k` lowercase letters from 'a' to the `k`-th letter of the alphabet, `j` is `k + 96`, and stdin is empty. If `k` is 1, a string of `n` lowercase letters 'a' is printed. If `k` is greater than 1, either `s` or 2 * `s` is printed, depending on whether `n` is 1 or not.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads two integers n and k, and prints a string of lowercase letters from 'a' to the k-th letter of the alphabet. If k is 1, it prints n repetitions of the letter 'a'. If k is greater than 1, it prints either one or two repetitions of the string, depending on whether n is 1 or not. After processing all test cases, stdin is empty.

