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
        
    #State: The loop has executed for a number of times equal to the number of test cases, which is a positive integer. For each test case, the maximum and minimum values of a list of integers have been found and printed. The list contains integers from 0 to n-1, where n is the input for each test case. The maximum value is the last element in the list, and the minimum value is the first element in the list. The loop has printed the maximum and minimum values for each test case.

#Overall this is what the function does:Finds and prints the maximum and minimum values of a list of integers for each test case, where the list contains integers from 0 to n-1 and n is the input for each test case. The function accepts a positive integer as input, representing the number of test cases, and prints the maximum and minimum values for each test case.

