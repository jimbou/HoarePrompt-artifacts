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
        
    #State: start and end are integers such that start <= end, t is an integer, results is a list of strings. If t is 0, results is an empty list. If t is greater than 0, results contains t strings, each of which is either 'yes' or 'no'. For each string in results, if the corresponding count_ones is 0 or even and not equal to 2 or '11' is not in the corresponding arr, the string is 'yes'. Otherwise, the string is 'no'.
    for r in results:
        print(r)
        
    #State: `start` and `end` are integers such that `start` <= `end`, `t` is an integer, `results` is a list of strings, `r` is the last string in the `results` list. If `t` is 0, `results` is an empty list. If `t` is greater than 0, `results` contains `t` strings, each of which is either 'yes' or 'no'. For each string in `results`, if the corresponding count_ones is 0 or even and not equal to 2 or '11' is not in the corresponding arr, the string is 'yes'. Otherwise, the string is 'no'. All strings in the `results` list have been printed.

#Overall this is what the function does:This function takes an integer input t, representing the number of test cases. For each test case, it reads an integer n and a binary string arr. It then checks the number of '1's in the string and appends 'yes' or 'no' to the results list based on the following conditions: if there are no '1's or an even number of '1's (not equal to 2) or '11' is not in the string, it appends 'yes'; otherwise, it appends 'no'. Finally, it prints all the strings in the results list.

