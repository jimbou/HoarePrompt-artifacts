#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of one integer (the size of the permutation) and a permutation of integers from 0 to n - 1, where n is the size of the permutation.
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
        
    #State: The loop has executed for the number of test cases specified in the input, and for each test case, the permutation has been sorted and the largest element has been identified and printed to the console. The output buffer is empty.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of a permutation of integers. For each test case, it identifies the largest element and its position in the permutation, and prints this information to the console. The function repeats this process for the specified number of test cases, ensuring that the output buffer is empty after completion.

