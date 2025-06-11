#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one integer n (2 <= n <= 10^4) followed by n integers p_0, p_1, ..., p_{n-1} representing a permutation of integers from 0 to n - 1.
    for _ in range(int(input())):
        n = int(input())
        
        mak = 0
        
        for i in range(1, n):
            print('?', mak, mak, i, i)
            sys.stdout.flush()
            if str(input()) == '<':
                mak = i
        
        mak2 = mak
        
        pans = []
        
        for i in range(n):
            print('?', mak, mak2, i, mak2)
            sys.stdout.flush()
            s = str(input())
            if s == '<':
                mak = i
                pans = [i]
            elif s == '=':
                pans.append(i)
        
        mak = 0
        
        for i in range(1, len(pans)):
            print('?', pans[mak], pans[mak], pans[i], pans[i])
            sys.stdout.flush()
            if str(input()) == '>':
                mak = i
        
        print('!', mak2, mak)
        
        sys.stdout.flush()
        
    #State: The output state will be a series of lines, each containing two integers separated by a space, representing the indices of the maximum and minimum elements in each permutation. The number of lines will be equal to the number of test cases.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains an integer n followed by a permutation of integers from 0 to n-1. It then determines the indices of the maximum and minimum elements in each permutation and prints them to standard output, one pair per line. The function iteratively queries the input to compare elements and find the maximum and minimum indices, and it handles multiple test cases.

