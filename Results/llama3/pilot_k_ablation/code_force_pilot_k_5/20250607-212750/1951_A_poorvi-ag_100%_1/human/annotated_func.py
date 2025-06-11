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
        
    #State: start is an integer, end is an integer, t is 0, n is an integer equal to the first input, arr is a string equal to the second input, _ is t, count_ones is an integer equal to the number of '1's in arr, stdin is empty, results is a list containing t strings. If count_ones is 0, all strings in results are 'yes'. If count_ones is not 0, if count_ones is odd, all strings in results are 'no'. If count_ones is even, all strings in results are 'yes' if count_ones is not 2 or '11' is not in arr, otherwise all strings in results are 'no'.
    for r in results:
        print(r)
        
    #State: The loop has finished executing, and all strings in the results list have been printed. The state of the other variables remains unchanged.

#Overall this is what the function does:This function reads a series of inputs from the user, where each input consists of an integer and a string. It then analyzes the string to determine if it meets certain conditions based on the count of '1's in the string. If the count is 0, it appends 'yes' to the results list. If the count is odd, it appends 'no'. If the count is even, it appends 'yes' unless the count is 2 and the string contains '11', in which case it appends 'no'. After processing all inputs, it prints out the results list.

