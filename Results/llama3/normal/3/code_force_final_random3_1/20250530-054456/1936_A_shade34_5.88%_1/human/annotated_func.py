#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (the number of elements in the sequence). The sequence is a permutation of integers from 0 to n - 1.
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
        
    #State: The loop has finished executing, the output buffer is empty, `n` is greater than or equal to 1, `i` is `n`, `s` is a string, `pans` is a list containing all values from 0 to `n-1`, `mak` is `n-1`, and `mak2` is `n-1`. The final output is printed: '!', `mak2`, and the value of `mak` which is `n-1`.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a sequence of integers from 0 to n-1. For each test case, it finds the maximum and second maximum elements in the sequence and prints them in the format '!', max, second_max. The function repeats this process for all test cases and then terminates, leaving the output buffer empty.

