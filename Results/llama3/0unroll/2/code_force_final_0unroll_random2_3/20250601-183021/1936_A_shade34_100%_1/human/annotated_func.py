#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of one integer (n) followed by n integers (p_0, p_1, ..., p_{n-1}) representing a permutation of integers from 0 to n - 1.
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
        
        print('!', mak2, pans[mak])
        
        sys.stdout.flush()
        
    #State: The output state after the loop executes all the iterations is a series of print statements in the format '!', each containing two values: the first value is the index of the maximum element in the permutation, and the second value is the index of the minimum element in the permutation. The number of print statements is equal to the number of test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case represents a permutation of integers. For each test case, it identifies the maximum and minimum elements in the permutation and prints their indices in the format '!', along with the index of the maximum element. The function performs a series of queries to determine the maximum and minimum elements, and it outputs the results for each test case.

