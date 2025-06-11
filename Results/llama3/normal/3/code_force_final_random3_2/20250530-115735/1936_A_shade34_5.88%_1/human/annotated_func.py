#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (n).
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
        
    #State: The loop has finished executing, and the output buffer is flushed. The value of `mak` is the last value of `i` for which the user input was '>'. If the user input was never '>', then `mak` remains 0. The value of `i` is `n`, and this is printed: '!', the value of `mak2` and the value of `mak`. The output buffer is flushed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer n. For each test case, it performs a series of queries to determine the maximum and second maximum values in a range from 1 to n. It then prints the second maximum value and the maximum value in the format '!, max, second_max'. The function repeats this process for all test cases and ensures that the output buffer is flushed after each test case.

