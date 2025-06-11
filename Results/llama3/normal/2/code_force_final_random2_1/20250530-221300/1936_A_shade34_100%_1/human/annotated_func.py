#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0). Then for each test case, stdin contains one input: an integer (greater than 1).
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
        
    #State: `n` is an integer greater than or equal to 0, `i` is `len(pans)-1`, `_` is `n-1`, `mak2` is the last `i` for which the input is '<', `pans` is a list containing at least `len(pans)` elements, the output buffer is flushed, and the specified messages are printed with the correct values of `mak`, `mak2`, and `i`. If the input is '>', then `s` is '>', `mak` is `len(pans)-1`. Otherwise, `s` is the input string and `mak` is 0. and this is printed: '!' followed by the last index for which the input is '<' which is `mak2` and the last element of the list `pans` which is `pans[mak]` and the output buffer is flushed.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents a test case with a value greater than 1. For each test case, the function performs a series of queries by printing specific messages to standard output, reading the responses from standard input, and updating its internal state based on the responses. The function ultimately prints a final message to standard output in the format '! <index> <value>', where <index> and <value> are determined by the internal state of the function after processing all test cases. The function also ensures that the output buffer is flushed after printing each message.

