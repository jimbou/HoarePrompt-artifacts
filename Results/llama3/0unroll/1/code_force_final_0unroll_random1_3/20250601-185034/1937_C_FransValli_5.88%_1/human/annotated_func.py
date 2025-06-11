#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (n).
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: The output state is the final state of the variables after the loop has executed all its iterations. The loop iterates over the range of the input integer (the number of test cases). For each test case, it iterates over the range of the input integer (n) to find the maximum value (k) and the second maximum value (best). The final output state is the state of the variables after the loop has finished executing all its iterations, which includes the values of k and best for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer 'n'. For each test case, it finds the maximum value 'k' and the second maximum value 'best' by querying the input in a specific format. It then prints the maximum value 'k' and the second maximum value 'best' for each test case in the format '! k best'. The function iterates over all test cases, and its final state is the output of the maximum and second maximum values for each test case.

