#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then t blocks of inputs. Each block contains an integer n and then a list of n integers. The sum of the integers in each block is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: t is an integer, _ is t, stdin is empty, n is not defined, arr is not defined.

#Overall this is what the function does:This function reads multiple blocks of input from stdin, where each block contains an integer n followed by a list of n integers. It checks if the list is sorted in ascending order and prints 'YES' if it is, and 'NO' otherwise. The function repeats this process for a number of blocks specified by the first integer input, t.

