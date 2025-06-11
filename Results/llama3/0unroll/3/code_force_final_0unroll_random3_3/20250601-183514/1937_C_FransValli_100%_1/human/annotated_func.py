#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of one integer (n) and a sequence p_0, p_1, \ldots, p_{n-1} , which is a permutation of \\{0,1,\ldots,n-1\\}.
    for _ in range(int(input())):
        n = int(input())
        
        maxi = 0
        
        for i in range(1, n):
            print('?', maxi, maxi, i, i, flush=True)
            res = input()
            if res == '<':
                maxi = i
        
        arr = [0]
        
        for i in range(1, n):
            print('?', maxi, arr[0], maxi, i, flush=True)
            res = input()
            if res == '<':
                arr = [i]
            elif res == '=':
                arr.append(i)
        
        mini = arr[0]
        
        for item in arr[1:]:
            print('?', mini, mini, item, item, flush=True)
            res = input()
            if res == '>':
                mini = item
        
        print('!', maxi, mini, flush=True)
        
    #State: The output state is a sequence of '!' statements, each containing the maximum and minimum values of the permutation for each test case. The '!' statements are printed to the standard output.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer (n) followed by a permutation of numbers from 0 to n-1. It then finds the maximum and minimum values in each permutation and prints them to standard output in the format '! maxi mini' for each test case.

