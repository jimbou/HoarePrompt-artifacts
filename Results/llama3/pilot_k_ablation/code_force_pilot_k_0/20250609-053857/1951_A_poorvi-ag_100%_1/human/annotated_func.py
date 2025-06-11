#State of the program right berfore the function call: start and end are integers such that start <= end.
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        arr = input()
        
        count_ones = arr.count('1')
        
        if count_ones == 0:
            results.append('yes')
        elif count_ones % 2 != 0:
            results.append('no')
        elif count_ones == 2:
            if '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('yes')
        
    #State: Output State: The loop has executed t times, and the results list contains t strings, each of which is either 'yes' or 'no', depending on the input strings. The values of start and end remain unchanged.
    for r in results:
        print(r)
        
    #State: Output State: The loop has executed t times, and the results list contains t strings, each of which is either 'yes' or 'no', depending on the input strings. The values of start and end remain unchanged.

#Overall this is what the function does:This function determines whether a given binary string can be rearranged into a valid binary string with alternating 1s and 0s. It takes no input parameters but reads input from the user, specifically an integer t representing the number of test cases, followed by t binary strings. The function then analyzes each binary string, counting the number of 1s and checking for the presence of consecutive 1s. Based on these conditions, it appends either 'yes' or 'no' to the results list, indicating whether the string can be rearranged into a valid alternating binary string. The function prints each result in the results list, effectively providing a verdict on the rearrangability of each input binary string.

