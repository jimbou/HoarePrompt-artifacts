#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3), representing the number of test cases. Each of the following lines contains a single integer n (3 <= n <= 10^5), representing the length of the permutation p. The sum of n over all test cases does not exceed 10^5.
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: `a` is an integer equal to t (1 <= t <= 10^3), `i` is `t-1`, `p` is a list of all integers from 1 to `a` inclusive, stdin is empty, and the list of all integers from 1 to `a` inclusive is being printed for all test cases.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a single integer representing the length of a permutation. It then generates a permutation of all integers from 1 to the given length, with even numbers appearing before odd numbers, and prints this permutation for each test case. The function processes all test cases and empties the standard input.

