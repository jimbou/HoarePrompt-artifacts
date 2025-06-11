#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (the size of the permutation).
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
        
    #State: The loop executes for a number of times equal to the number of test cases, and for each test case, it finds the maximum value in the permutation and prints it along with its index. The output buffer is flushed after each print statement.

#Overall this is what the function does:The function reads a number of test cases from standard input, then for each test case, it reads the size of a permutation and finds the maximum value in the permutation along with its index by querying the input in a specific manner. It prints the maximum value and its index for each test case, flushing the output buffer after each print statement.

