#State of the program right berfore the function call: stdin contains one input: an integer
    return int(putin())
    #The program returns an integer that was provided as input through stdin.

#Overall this is what the function does:The function reads an integer from standard input and returns it as an integer value.

#State of the program right berfore the function call: putin() is a function that returns a string of space-separated integers.
    return map(int, putin().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a string of space-separated integers returned by the putin() function into an integer.

#Overall this is what the function does:The function takes no parameters and returns a map object containing a sequence of integers. The integers are the result of converting a string of space-separated integers into individual integers. The function relies on the putin() function to provide the string of space-separated integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of pairs of integers, where each pair represents the prices of an item for Alice and Bob, respectively.
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` is a list of pairs of integers, `sec_arr` is an empty list, `sub_summ` is the sum of all the first elements of the pairs in the initial `sec_arr`, `val_a` is the last pair of integers in the initial `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `main_ar` is a list of pairs of integers, `sec_arr` is an empty list, `sub_summ` is the sum of all the first elements of the pairs in the initial `sec_arr` plus the sum of all pairs of integers in `main_ar` where the sum of the pair is greater than or equal to 0, `val_a` is the last pair of integers in the initial `sec_arr`.
    return sub_summ
    #The program returns the sum of all the first elements of the pairs in the initial `sec_arr` plus the sum of all pairs of integers in `main_ar` where the sum of the pair is greater than or equal to 0. Since `sec_arr` is an empty list, the sum of its first elements is 0. The sum of all pairs of integers in `main_ar` where the sum of the pair is greater than or equal to 0 is calculated based on the pairs in `main_ar`.

#Overall this is what the function does:This function calculates the sum of all pairs of integers in the input list `main_ar` where the sum of the pair is greater than or equal to 0, and returns this sum. The input list `sec_arr` is not used in the calculation, but its initial state is used to initialize a variable `sub_summ` to 0. The function does not modify the input lists.

