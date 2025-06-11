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
        #The program returns nothing because there is no return statement with a value or variable. The current state of the program remains unchanged, with x being 2, 1 being printed, and 0 being printed. The list subseq_lens remains empty, and mx remains 0.
    #State: *x is an integer between 1 and 1000, x is not equal to 2, stdin contains 1 input: t space-separated integers, subseq_lens is an empty list, mx is 0
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
        
    #State: x is 0, subseq_lens is a list of integers representing the lengths of the subsequences of consecutive powers of 2 that sum up to the original value of x, mx is the maximum length of these subsequences, and stdin contains 1 input: t space-separated integers.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `x` is 0, `subseq_lens` is a list of integers that must have at least `len(subseq_lens)` elements, `mx` is the maximum length of these subsequences, `ansv` is a list of integers from 0 to `mx-1` plus all elements of `subseq_lens` except the first one, `i` is `len(subseq_lens)-1`, and stdin contains 1 input: t space-separated integers.
    print(len(ansv))
    #This is printed: 2 times i plus 1 (where i is len(subseq_lens)-1)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `x` is 0, `subseq_lens` is a list of integers that must have at least `len(subseq_lens)` elements, `mx` is the maximum length of these subsequences, `ansv` is a list of integers from 0 to `mx-1` plus all elements of `subseq_lens` except the first one and must have at least `len(ansv)` elements, `i` is `len(ansv)-1`, and stdin contains 1 input: t space-separated integers, and all elements of the list `ansv` are printed.
    print()
    #This is printed: Nothing

#Overall this is what the function does:This function reads an integer input from stdin, representing the number of subsequences of consecutive powers of 2 that sum up to the original value. If the input is 2, it prints 1 and 0 and returns without modifying the state. Otherwise, it calculates the lengths of these subsequences, finds the maximum length, and constructs a list of integers from 0 to the maximum length minus 1, plus all subsequence lengths except the first one. It then prints the length of this list and its elements, separated by spaces. The function does not return any value or modify the input variables, but instead prints the results to stdout.

