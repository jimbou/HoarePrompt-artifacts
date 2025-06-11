#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the values of X for each test case). Each integer is a positive integer greater than 1.
    x = int(input())
    subseq_lens = []
    mx = 0
    if (x == 2) :
        print(1)
        #This is printed: 1
        print(0)
        #This is printed: 0
        return
        #The program returns nothing, as the return statement is empty. The value of x remains 2, subseq_lens remains an empty list, and mx remains 0. The input from stdin is still a list of integers, and the printed output is still "1" and "0".
    #State: *x is a positive integer, subseq_lens is an empty list, mx is 0, stdin contains 1 input: a list of integers, and x is not equal to 2
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
        
    #State: x is 0, subseq_lens is a list of integers, mx is the maximum value in subseq_lens, and stdin is empty.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `x` is 0, `subseq_lens` is a list of integers, `mx` is the maximum value in `subseq_lens`, `ansv` is a list of integers from 0 to `mx-1` and then the rest of the integers in `subseq_lens` starting from index 1, and stdin is empty.
    print(len(ansv))
    #This is printed: the length of the list ansv (which is equal to the length of subseq_lens plus the number of integers from 0 to mx-1)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: Output State: The output state after the loop executes all the iterations is that the value of `i` is `mx` and the standard output contains the string representation of the list `ansv` with each element separated by a space.
    print()
    #This is printed: an empty line

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to the standard output. It accepts a positive integer x and a list of integers as input. If x is 2, it prints "1" and "0" and returns without modifying the input. Otherwise, it generates a list of integers (subseq_lens) by repeatedly subtracting the largest power of 2 less than or equal to x, and keeps track of the maximum value (mx) in this list. It then constructs a new list (ansv) by concatenating a list of integers from 0 to mx-1 with the rest of the integers in subseq_lens starting from index 1. Finally, it prints the length of ansv and the elements of ansv separated by spaces, followed by an empty line.

