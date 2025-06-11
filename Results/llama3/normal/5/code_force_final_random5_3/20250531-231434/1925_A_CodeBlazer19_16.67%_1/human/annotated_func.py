#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 ≤ t ≤ 676). Each of the following t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
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
        
    #State: `t` is an integer between 1 and 676 (inclusive), `i` is `t`, `n` is an integer, `k` is an integer, `s` is a string containing `k` characters from 'a' to the character represented by the ASCII value `k + 96`, `stdin` is empty, `j` is `k + 96`. If `k` is 1, a string of 'n' repetitions of the character 'a' is printed. If `k` is not 1, either 2 times the string `s` or the string `s` is printed, depending on whether `n` is equal to 1 or not.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. The function reads an integer t, representing the number of test cases, and then reads t pairs of integers n and k. For each pair, it constructs a string s containing k characters from 'a' to the character represented by the ASCII value k + 96. If k is 1, it prints a string of n repetitions of the character 'a'. If k is not 1, it prints either 2 times the string s or the string s, depending on whether n is equal to 1 or not. After processing all test cases, the function leaves stdin empty.

