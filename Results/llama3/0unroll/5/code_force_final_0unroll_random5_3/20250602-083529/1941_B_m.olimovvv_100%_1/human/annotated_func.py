#State of the program right berfore the function call: stdin contains multiple inputs: first an integer, then a series of pairs of inputs where the first input of each pair is an integer and the second input is a space-separated list of integers. The first integer is a non-negative integer and represents the number of pairs of inputs that follow. The first integer of each pair is a non-negative integer and represents the length of the list of integers that follows. The list of integers is a list of non-negative integers.
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: Output State: The output state is a series of 'YES' or 'NO' strings, each indicating whether the corresponding list of integers can be reduced to zeros by the given operations.

#Overall this is what the function does:The function reads multiple pairs of inputs from stdin, where each pair consists of an integer and a list of integers. For each pair, it checks if the list can be reduced to zeros by repeatedly subtracting twice the current element from the next element and the current element from the element after next, starting from the first element. If the list can be reduced to zeros, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for the specified number of pairs, printing a 'YES' or 'NO' for each pair.

