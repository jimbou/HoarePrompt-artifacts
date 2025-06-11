#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t space-separated integers (2 <= X <= 10^18).
    x = int(input())
    subseq_lens = []
    mx = 0
    if (x == 2) :
        print(1)
        #This is printed: 1
        print(0)
        #This is printed: 0
        return
        #The program returns nothing, as the return statement is empty. The values of the variables remain unchanged: x is still an integer equal to 2, subseq_lens is still an empty list, and mx is still 0. The input from stdin has been read, but its value is not used in the program. The output of the program is still 1, and the printed value is still 0.
    #State: x is an integer between 1 and 1000, but not equal to 2, subseq_lens is an empty list, mx is 0, stdin contains 1 input: a space-separated list of integers.
    while x != 0:
        i = 0
        
        while 2 ** i <= x:
            i += 1
        
        if i == 0:
            break
        else:
            subseq_lens.append(i - 1)
            x -= 2 ** (i - 1)
            mx = max(mx, i - 1)
        
    #State: x is 0, subseq_lens is a list of integers, mx is an integer, i is the smallest integer greater than or equal to log2(x) + 1, stdin contains 1 input: a space-separated list of integers.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `x` is 0, `subseq_lens` is a list of integers, `mx` is an integer, `i` is equal to the length of `subseq_lens`, `ansv` is a list of integers from 0 to `mx-1` and also includes all elements of `subseq_lens` except the first one at the end, stdin contains 1 input: a space-separated list of integers.
    print(len(ansv))
    #This is printed: mx + len(subseq_lens) - 1
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `x` is 0, `subseq_lens` is a list of integers, `mx` is an integer, `i` is equal to the length of `ansv`, `ansv` is a list of integers from 0 to `mx-1` and also includes all elements of `subseq_lens` except the first one at the end, stdin contains 1 input: a space-separated list of integers, and all elements of the list `ansv` are printed.
    print()
    #This is printed: nothing (an empty line)

#Overall this is what the function does:This function reads an integer and a list of integers from standard input, processes the list by repeatedly subtracting the largest power of 2 less than or equal to the current number, and prints the length of the resulting list and its elements. If the input integer is 2, it prints 1 and 0 and returns without processing the list. Otherwise, it constructs a list of integers from 0 to the maximum power of 2 minus 1 and appends all elements of the processed list except the first one, then prints the length of this list and its elements.

