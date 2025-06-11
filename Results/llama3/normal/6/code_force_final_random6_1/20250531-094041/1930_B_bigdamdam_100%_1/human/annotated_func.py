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
        
    #State: n is an integer greater than or equal to 3, p is a list of n integers where every other element starting from the first is n, n-2, n-4, ..., n-2*floor(n/2), and the rest are zeros except for the ith element which is n-1, ind is n+1, i is n, stdin is empty, and the list p is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n representing the length of a permutation. It then generates a permutation of length n, where every other element starting from the first is n, n-2, n-4, ..., n-2*floor(n/2), and the rest are zeros except for the ith element which is n-1. The function prints each generated permutation.

