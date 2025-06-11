#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    return int(putin())
    #The program returns an integer greater than 0 that was provided as input from stdin.

#Overall this is what the function does:The function reads an integer greater than 0 from standard input and returns it as an integer.

#State of the program right berfore the function call: putin() returns a string containing a space-separated list of integers.
    return map(int, putin().split())
    #The program returns a map object that contains a sequence of integers, where each integer is a result of converting a string from the space-separated list of integers returned by putin() to an integer.

#Overall this is what the function does:Converts a string of space-separated integers into a sequence of integers and returns it as a map object.

#State of the program right berfore the function call: main_ar and sec_arr are lists of pairs of integers, where each pair represents the prices of an item for Alice and Bob, respectively.
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: Output State: `main_arr` and `sec_arr` are lists of pairs of integers, where each pair represents the prices of an item for Alice and Bob, respectively; `sub_summ` is the sum of the prices of all items for Bob.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: Output State: `main_arr` and `sec_arr` are lists of pairs of integers, where each pair represents the prices of an item for Alice and Bob, respectively; `sub_summ` is the sum of the prices of all items for Bob, where the prices are only considered if the sum of the prices for Alice and Bob is greater than or equal to 0.
    return sub_summ
    #The program returns the sum of the prices of all items for Bob, where the prices are only considered if the sum of the prices for Alice and Bob is greater than or equal to 0.

#Overall this is what the function does:Functionality: This function calculates the sum of prices for Bob from two lists of pairs of integers representing prices for Alice and Bob. It only considers prices where the combined price for Alice and Bob is greater than or equal to 0. The function returns this calculated sum, leaving the input lists unchanged.

