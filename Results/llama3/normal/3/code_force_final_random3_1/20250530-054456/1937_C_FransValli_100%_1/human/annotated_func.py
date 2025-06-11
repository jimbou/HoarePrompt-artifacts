#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (the size of the permutation).
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
        
    #State: The loop has executed for the number of test cases specified in the input, and for each test case, the maximum and minimum elements in the permutation have been found and printed.

#Overall this is what the function does:This function reads a number of test cases from standard input, then for each test case, it reads the size of a permutation and finds the maximum and minimum elements in the permutation by querying the input stream. It prints the maximum and minimum elements for each test case. The function does not modify the input permutation.

