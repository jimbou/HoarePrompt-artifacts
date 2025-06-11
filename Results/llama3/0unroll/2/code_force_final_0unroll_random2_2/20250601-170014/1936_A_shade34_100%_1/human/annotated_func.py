#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases) followed by a series of test cases. Each test case consists of one integer (the size of the permutation) followed by the permutation itself (a list of integers).
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
        
    #State: The output state after the loop executes all the iterations is a series of answers for each test case, where each answer is in the format "! a b" (without quotes), with "a" being the index of the maximum element in the permutation and "b" being the index of the minimum element in the permutation. The number of answers is equal to the number of test cases.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a permutation of integers. For each test case, it determines the indices of the maximum and minimum elements in the permutation and prints the result in the format "! a b", where "a" is the index of the maximum element and "b" is the index of the minimum element. The function repeats this process for all test cases provided in the input.

