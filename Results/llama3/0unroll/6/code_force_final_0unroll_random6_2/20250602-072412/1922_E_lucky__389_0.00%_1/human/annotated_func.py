#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t integers (X). t is a positive integer and 2 <= X <= 10^18.
    x = int(input())
    x -= 1
    subseq_lens = []
    mx = 0
    while x != 0:
        i = 0
        
        while 2 ** (i + 1) <= x + 1:
            i += 1
        
        if i == 0:
            break
        else:
            subseq_lens.append(i)
            x -= 2 ** i - 1
            mx = max(mx, i)
        
    #State: x is 0, subseq_lens is [3, 2, 1], mx is 3.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `x` is 0, `subseq_lens` is [3, 2, 1], `mx` is 3, `ansv` is [0, 1, 2, 2, 1].
    print(len(ansv))
    #This is printed: 5
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: Output State: `x` is 0, `subseq_lens` is [3, 2, 1], `mx` is 3, `ansv` is [0, 1, 2, 2, 1], and the length of `ansv` which is 5 is being printed, and the numbers 0, 1, 2, 2, 1 are printed in that order.
    print()
    #This is printed: 5 (which is the length of ansv), 0, 1, 2, 2, 1 (which are the elements of ansv)

#Overall this is what the function does:This function reads an integer input from the user, subtracts 1 from it, and then repeatedly subtracts the largest power of 2 minus 1 from the result until it reaches 0. It keeps track of the powers of 2 used in this process and stores them in a list. The function then generates a new list by concatenating a list of numbers from 0 to the maximum power of 2 used, with the list of powers of 2 used, excluding the first element. Finally, it prints the length of the new list and its elements in order.

