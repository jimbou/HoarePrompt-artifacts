#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases) followed by the description of the test cases. Each test case description contains one integer (n) followed by a permutation p of integers from 0 to n - 1.
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
        
    #State: The loop will execute for the number of test cases specified in the input. For each test case, it will determine the maximum value in the permutation and its position, and then find the second maximum value and its position. Finally, it will print the position of the second maximum value and the value itself. The output will be in the format "! <position> <value>" for each test case.

#Overall this is what the function does:Determines and prints the position and value of the second maximum element in a permutation for multiple test cases.

