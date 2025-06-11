#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing an integer X (2 <= X <= 10^18).
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
        
    #State: stdin contains 1 input: an integer, x is 0, subseq_lens is a list of integers, mx is the maximum of 0 and the greatest integer i such that 2^i - 1 <= x
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: x is 0, subseq_lens is a list of integers, mx is 0, ansv is a list containing an empty list and all elements of subseq_lens except the first one, i is len(subseq_lens) - 1, stdin contains 1 input: an integer.
    print(len(ansv))
    #This is printed: len(subseq_lens) - 1
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: The loop has finished executing, and the output state is: `x` is 0, `subseq_lens` is a list of integers, `mx` is 0, `ansv` is a list containing an empty list and all elements of `subseq_lens` except the first one, `i` is equal to the length of `subseq_lens`, `stdin` contains 1 input: an integer, and all elements of `ansv` have been printed.
    print()
    #This is printed: a blank line

#Overall this is what the function does:This function reads an integer t from standard input, then reads t lines each containing an integer X. It decomposes each X into a sequence of integers representing the lengths of subsequences, where each subsequence is a contiguous sequence of bits in the binary representation of X. The function then prints the length of the sequence of subsequence lengths, followed by the sequence of subsequence lengths, excluding the first subsequence length. Finally, it prints a blank line.

