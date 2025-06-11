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
        
    #State: The output state after the loop executes all the iterations is the number of test cases, followed by the results of each test case. Each test case result consists of two integers, the first representing the maximum value in the range [1, n] and the second representing the index of the maximum value in the range [1, n]. The output state is in the format: "number of test cases\nresult1\nresult2\n...\nresultn", where each result is in the format "mak2 mak".

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer n. For each test case, it finds the maximum value and its index in the range [1, n] by querying the input stream and then outputs the result in the format "maximum value index". The function repeats this process for all test cases and outputs the results in the format "number of test cases\nresult1\nresult2\n...\nresultn".

