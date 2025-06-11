#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases) followed by a series of test cases. Each test case contains one integer (n) followed by a permutation of integers from 0 to n - 1.
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
        
    #State: The loop has finished executing, and the final output state is determined by the last iteration of the loop. The value of `n` is the number of test cases, `i` is `len(pans)-1`, `pans` is a list containing all indices `i` such that the input string is '=' at iteration `i`, `mak2` is the largest index `i` such that the input string is '<' at iteration `i`, and `mak` is the index of the maximum value in `pans`. The output buffer has been flushed a total of `n+len(pans)+n+len(pans)+1` times. The final output is '!' followed by the value of `mak2` and the value of `pans[mak]`.

#Overall this is what the function does:The function reads input from stdin, processes a series of test cases, and outputs the results to stdout. For each test case, it finds the maximum value in a permutation of integers and its corresponding index, and then outputs the index of the maximum value and the value itself. The function iteratively queries the input to determine the maximum value and its index, and it flushes the output buffer after each query and after the final output. The function processes all test cases and produces a final output in the format '! <index> <value>'.

