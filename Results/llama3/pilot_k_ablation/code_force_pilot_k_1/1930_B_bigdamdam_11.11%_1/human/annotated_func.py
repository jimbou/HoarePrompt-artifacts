#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^3) — the number of test cases. Each test case contains a single integer n (3 <= n <= 10^5) — the length of the permutation p.
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: `i` is `t`, `a` is an integer between 3 and 10^5, `p` is an empty list, stdin is empty, and all integers between 1 and `a` inclusive for each test case have been printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains a single integer representing the length of a permutation. It then generates a permutation of integers from 1 to the given length, with even numbers appearing before odd numbers, and prints the permutation. The function repeats this process for all test cases, ultimately consuming all input and producing the corresponding permutations as output.

