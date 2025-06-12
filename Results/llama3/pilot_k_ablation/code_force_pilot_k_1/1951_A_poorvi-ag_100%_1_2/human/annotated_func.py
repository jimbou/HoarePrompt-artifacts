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
        
    #State: start and end are integers such that start is less than or equal to end, t is a non-negative integer, results is a list of strings, where each string is either 'yes' or 'no', stdin contains -t inputs. If t is 0, results is an empty list. If t is greater than 0, results contains t strings, each of which is 'yes' if the corresponding input string has an even number of '1's and no consecutive '1's, or if the number of '1's is a multiple of 4, and 'no' otherwise.
    for r in results:
        print(r)
        
    #State: start and end are integers such that start is less than or equal to end, t is a non-negative integer, results is a list of strings, where each string is either 'yes' or 'no', stdin contains -t inputs. If t is 0, results is an empty list. If t is greater than 0, results contains t strings, each of which is 'yes' if the corresponding input string has an even number of '1's and no consecutive '1's, or if the number of '1's is a multiple of 4, and 'no' otherwise. All strings in the results list have been printed.

#Overall this is what the function does:This function reads a non-negative integer t from standard input, followed by t strings. For each string, it checks if the number of '1's is even and there are no consecutive '1's, or if the number of '1's is a multiple of 4. If either condition is met, it appends 'yes' to the results list; otherwise, it appends 'no'. Finally, it prints all the strings in the results list.

