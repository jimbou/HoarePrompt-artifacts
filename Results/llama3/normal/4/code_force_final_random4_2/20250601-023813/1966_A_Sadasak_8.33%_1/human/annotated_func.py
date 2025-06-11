#State of the program right berfore the function call: arr is a list of integers, k is an integer, and 2 <= k <= 100.
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is a list of integers, `k` is an integer and 2 <= k <= 100, `frequency_table` is a dictionary where the keys are all the integers in the list `arr` and the values are `k` if the original value of `frequency_table[num]` is greater than `k`. Otherwise, the value of `frequency_table` is the frequency of the integer in the list `arr`.
    return frequency_table
    #The program returns a dictionary where the keys are all the integers in the list `arr` and the values are `k` if the original frequency of the integer in the list `arr` is greater than `k`. Otherwise, the value is the frequency of the integer in the list `arr`. The value of `k` is an integer between 2 and 100 (inclusive).

#Overall this is what the function does:Functionality: This function takes a list of integers and an integer k as input, and returns a dictionary where the keys are the integers from the list and the values are their frequencies, but capped at k. In other words, if an integer appears more than k times in the list, its frequency in the returned dictionary will be k; otherwise, its frequency will be its actual count in the list.

