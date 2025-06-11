#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: `t` is an integer between 0 and 49 (inclusive), `n` is an integer, `_` is `t`, stdin contains no input. If `n` is an odd number, 'NO' is printed. If `n` is an even number, 'YES' is printed, pattern is a list of 'A's and 'B's with a length of `n`, `i` is `n // 2 - 1`, and a string of 'A's and 'B's with a length of `n` is printed. The string contains alternating 'A's and 'B's if `n` is even, otherwise 'NO' is printed. If `n` is at least 50, pattern is a list of 'A's and 'B's with a length of `n`.

#Overall this is what the function does:This function reads an integer `t` from standard input, representing the number of test cases, and then for each test case, it reads another integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it prints 'YES' and then generates a string of alternating 'A's and 'B's of length `n`, which it also prints. The function repeats this process `t` times, consuming all input from standard input.

