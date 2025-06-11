#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (n).
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
        
    #State: The loop has executed all iterations, and the output state is the final state of the variables after the last iteration. The variable 'maxi' holds the maximum value found in the last test case, 'mini' holds the minimum value found in the last test case, and 'arr' holds the list of values that are equal to the minimum value found in the last test case. The input buffer is empty, and the output buffer contains the results of all the print statements executed during the loop iterations.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer 'n'. For each test case, it finds the maximum and minimum values within a range of 1 to 'n' by querying the input buffer and updates the output buffer with the results. The function iterates through all test cases, and after the last iteration, it outputs the maximum and minimum values found in the last test case, along with the list of values equal to the minimum value. The function does not return any values but modifies the output buffer with the results of all test cases.

