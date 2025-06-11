#State of the program right berfore the function call: arr is a list of integers, k is an integer, and 2 <= k <= 100.
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: `arr` is a list of integers, `k` is an integer, and 2 <= k <= 100, `frequency_table` is a dictionary where each key is an integer from the list `arr` and each value is the frequency of that integer in `arr`, capped at `k`.
    return frequency_table
    #The program returns a dictionary where each key is an integer from the list `arr` and each value is the frequency of that integer in `arr`, capped at `k`, where `k` is an integer between 2 and 100 (inclusive).

#Overall this is what the function does:This function takes a list of integers and an integer k as input, and returns a dictionary where each key is an integer from the list and its corresponding value is the frequency of that integer in the list, capped at k. The function effectively counts the occurrences of each integer in the list, but limits the count to a maximum of k.

