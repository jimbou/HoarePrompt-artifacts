#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3), representing the number of test cases. Each of the following lines contains a single integer n (3 <= n <= 10^5), representing the length of the permutation p.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(range(1, n + 1))
        
        for i in range(n // 2):
            a[2 * i + 1] = n - i
            a[2 * i] = i + 1
        
        if len(a) % 2 == 1:
            a[n - 1] = n // 2 + 1
        
        print(*a)
        
    #State: `n` is an integer greater than or equal to 0, `a` is a list of integers where the value at index 2*i is i+1 and the value at index 2*i+1 is n-i. If the length of `a` is odd, the value at index n-1 is n//2 +1. `_` is t-1, `i` is n // 2, stdin contains multiple lines of input minus t+1 lines that were read by input() function, and the list `a` is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a single integer n representing the length of a permutation. For each test case, it generates a permutation of the numbers from 1 to n, rearranging them in a specific pattern, and prints the resulting permutation. The pattern is such that the value at index 2*i is i+1 and the value at index 2*i+1 is n-i. If the length of the permutation is odd, the value at the last index is set to n//2 + 1. The function processes all test cases and prints the corresponding permutations.

