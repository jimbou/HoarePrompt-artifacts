#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3), representing the number of test cases. Each of the following lines contains a single integer n (3 <= n <= 10^5), representing the length of the permutation p.
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: The output state contains multiple lines of output. Each line contains a permutation of integers from 1 to n, where n is the length of the permutation. The permutation is constructed by alternating between the largest and smallest remaining integers, starting from the largest. The first line contains the permutation for the first test case, the second line contains the permutation for the second test case, and so on.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer representing the length of a permutation. It then generates a permutation of integers from 1 to the given length, constructed by alternating between the largest and smallest remaining integers, starting from the largest. The function prints each generated permutation on a separate line, resulting in multiple lines of output.

