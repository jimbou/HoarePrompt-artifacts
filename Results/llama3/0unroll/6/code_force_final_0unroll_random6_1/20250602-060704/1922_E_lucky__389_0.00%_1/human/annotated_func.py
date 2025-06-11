#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of integers (the test cases), each of which is a positive integer (X) such that 2 <= X <= 10^18.
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
        
    #State: x = 0, subseq_lens = [3, 2, 1], mx = 3
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `x` is 0, `subseq_lens` is [3, 2, 1], `mx` is 3, `ansv` is [0, 1, 2, 2, 1].
    print(len(ansv))
    #This is printed: 5 (which is the length of the list ansv)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: Output State: `i` is 5, `ansv` is [0, 1, 2, 2, 1], and the length of `ansv` which is 5 is being printed.
    print()
    #This is printed: 5

#Overall this is what the function does:This function reads a series of integers from standard input, representing test cases, and generates a sequence of integers based on the length of the longest subsequence that can be formed from the test cases. The function then prints the length of the generated sequence and the sequence itself.

