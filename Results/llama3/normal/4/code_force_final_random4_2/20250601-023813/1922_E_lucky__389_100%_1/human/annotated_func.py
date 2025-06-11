#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the values of X for each test case). Each value of X is a positive integer greater than or equal to 2 and less than or equal to 10^18.
    x = int(input())
    subseq_lens = []
    mx = 0
    if (x == 2) :
        print(1)
        #This is printed: 1
        print(0)
        #This is printed: 0
        return
        #The program returns nothing because the return statement is empty. The value of x is still 2, subseq_lens is still an empty list, and mx is still 0. The numbers 1 and 0 have been printed.
    #State: *stdin contains 1 input: a list of integers, x is an integer and is not equal to 2, subseq_lens is an empty list, mx is 0
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
        
    #State: x is 0, subseq_lens contains the base-2 logarithm of the original value of x plus 1, mx is the maximum of the original value of mx and the base-2 logarithm of the original value of x plus 1, stdin contains 1 input: a list of integers.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `x` is 0, `subseq_lens` contains the base-2 logarithm of the original value of `x` plus 1 and must have at least `len(subseq_lens)` elements, `mx` is the original value of `mx`, `ansv` is a list of integers from 0 to the original value of `mx` minus 1 and all elements of `subseq_lens` except the first one, stdin contains 1 input: a list of integers, `i` is `len(subseq_lens) - 1`
    #
    #The output state after the loop executes all the iterations is the same as the initial state, except that `ansv` now includes all elements of `subseq_lens` except the first one, and `i` is now equal to `len(subseq_lens) - 1`. The loop has iterated over all elements of `subseq_lens` and appended them to `ansv`, except for the first element which is not included in the loop.
    print(len(ansv))
    #This is printed: mx + len(subseq_lens) - 1
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `x` is 0, `subseq_lens` contains the base-2 logarithm of the original value of `x` plus 1 and must have at least `len(subseq_lens)` elements, `mx` is the original value of `mx`, `ansv` is a list of integers from 0 to the original value of `mx` minus 1 and all elements of `subseq_lens` except the first one and must have at least `len(ansv)` elements, stdin contains 1 input: a list of integers, `i` is `len(ansv) - 1`, and all elements of the list `ansv` are printed
    print()
    #This is printed: a newline character (an empty line)

#Overall this is what the function does:This function reads an integer from standard input, representing the number of test cases. If the number of test cases is 2, it prints 1 and 0 and returns without any further action. Otherwise, it reads a list of integers from standard input, calculates the base-2 logarithm of each integer plus 1, and stores these values in a list. It then generates a new list containing integers from 0 to the maximum base-2 logarithm minus 1, followed by all the calculated base-2 logarithms except the first one. The function prints the length of this new list, followed by its elements, and finally prints a newline character.

