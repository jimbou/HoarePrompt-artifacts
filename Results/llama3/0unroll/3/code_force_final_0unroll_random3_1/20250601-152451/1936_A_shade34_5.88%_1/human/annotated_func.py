#State of the program right berfore the function call: stdin contains one input: an integer (t) (1 <= t <= 10^3) followed by t test cases. Each test case contains one integer (n) (2 <= n <= 10^4).
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
        
    #State: The loop will output the indices of the maximum and second maximum elements in each test case, in the format "! mak2 mak", where mak2 is the index of the maximum element and mak is the index of the second maximum element. The indices are 1-based.

#Overall this is what the function does:This function reads input from standard input, where the first line contains an integer t (1 <= t <= 10^3) representing the number of test cases. For each test case, it reads an integer n (2 <= n <= 10^4) and then finds the indices of the maximum and second maximum elements in a sequence of n elements. The function outputs the indices of the maximum and second maximum elements for each test case in the format "! mak2 mak", where mak2 is the index of the maximum element and mak is the index of the second maximum element. The indices are 1-based.

