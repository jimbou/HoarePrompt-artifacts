#State of the program right berfore the function call: arr is a list of integers, k is an integer such that 2 <= k <= 100, and the length of arr is equal to n where 1 <= n <= 100.
    frequency_table = {}
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        
        if frequency_table[num] > k:
            frequency_table[num] = k
        
    #State: Output State: `arr` is a list of integers, `k` is an integer such that 2 <= k <= 100, the length of `arr` is equal to `n` where 1 <= n <= 100, and `frequency_table` is a dictionary where each key is a unique integer from `arr` and its corresponding value is the frequency of that integer in `arr`, capped at `k`.
    return frequency_table
    #The program returns a dictionary called `frequency_table` where each key is a unique integer from the list `arr` and its corresponding value is the frequency of that integer in `arr`, capped at `k`. The dictionary contains at most `k` unique integers from `arr`, where `k` is an integer between 2 and 100 (inclusive), and the length of `arr` is between 1 and 100 (inclusive).

#Overall this is what the function does:This function generates a frequency table from a given list of integers, capping the frequency of each integer at a specified value k. It returns a dictionary where each key is a unique integer from the list and its corresponding value is the frequency of that integer, limited to k. The function accepts a list of integers and an integer k as input, and the length of the list and the value of k are constrained to be within specific ranges. The function does not modify the original list.

