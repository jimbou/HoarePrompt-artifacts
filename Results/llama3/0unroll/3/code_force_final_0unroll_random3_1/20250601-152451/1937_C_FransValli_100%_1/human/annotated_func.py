#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (the number of elements in the sequence).
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
        
    #State: The output state is a series of print statements that output the maximum and minimum values of the sequence for each test case. The number of print statements is equal to the number of test cases. Each print statement is in the format '! maxi mini', where maxi is the maximum value and mini is the minimum value of the sequence. The stdin contains the same input as the initial state, which is an integer representing the number of test cases, followed by the number of elements in each sequence.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains a sequence of integers. For each test case, it determines the maximum and minimum values in the sequence through a series of queries and prints the maximum and minimum values in the format '! maxi mini'. The function repeats this process for each test case, ultimately producing a series of print statements that output the maximum and minimum values for each sequence.

