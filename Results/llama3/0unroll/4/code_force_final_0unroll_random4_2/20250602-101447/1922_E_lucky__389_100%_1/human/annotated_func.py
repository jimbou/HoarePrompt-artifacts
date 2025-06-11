#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the test cases). Each test case is a positive integer.
    x = int(input())
    subseq_lens = []
    mx = 0
    if (x == 2) :
        print(1)
        #This is printed: 1
        print(0)
        #This is printed: 0
        return
        #The program returns nothing, as the return statement is empty. The current state of the variables remains unchanged: x is 2, subseq_lens is an empty list, mx is 0, and stdin still contains 1 input: a list of integers. Additionally, the numbers 1 and 0 have been printed.
    #State: x is an integer, subseq_lens is an empty list, mx is 0, stdin contains 1 input: a list of integers, and x is not equal to 2
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
        
    #State: x is 0, subseq_lens is a list of integers, mx is an integer, and stdin is empty.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `x` is 0, `subseq_lens` is a list of integers, `mx` is an integer, `ansv` is a list of integers from 0 to `mx-1` followed by all integers from `subseq_lens` starting from index 1.
    print(len(ansv))
    #This is printed: mx + (length of subseq_lens - 1)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: Output State: The length of `ansv` has been printed, and all the elements of `ansv` have been printed to the console, separated by spaces.
    print()
    #This is printed: a newline character

#Overall this is what the function does:This function reads an integer and a list of integers from standard input, processes the list to generate a new list of integers, and prints the length and elements of the new list to the console. If the input integer is 2, it prints 1 and 0 and returns without further processing. Otherwise, it generates the new list by finding the maximum length of subsequences in the input list and appending the lengths of the subsequences to the new list. The function does not return any value but prints the results to the console.

