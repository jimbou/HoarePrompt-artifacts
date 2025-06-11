#State of the program right berfore the function call: stdin contains one input: an integer (greater than 1).
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
        
    #State: The loop will execute until the initial input integer is reached, and the final output state will be the last printed statement '! [maxi] [mini]', where 'maxi' is the maximum value found in the last iteration and 'mini' is the minimum value found in the last iteration.

#Overall this is what the function does:This function accepts an integer input from the user, representing the number of iterations. For each iteration, it finds the maximum and minimum values within a range of numbers (from 1 to the current iteration number) by querying the user through a series of comparison questions. After determining the maximum and minimum values, it prints the result in the format '! [maxi] [mini]'. The function repeats this process until the initial input integer is reached, providing the maximum and minimum values for each iteration.

