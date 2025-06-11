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
        
    #State: `start` is an integer, `end` is an integer, `t` is 0, `n` is an integer, `arr` is a string, `_` is `t`, `count_ones` is an integer, `results` is a list containing either 'yes' or 'no' depending on the value of `count_ones` for each iteration of the loop. If `count_ones` is 0, `results` has `t` 'yes' appended to it. If `count_ones` is not 0, then if `count_ones` is odd, `results` contains `t` 'no's. If `count_ones` is even, `results` contains 'no' if `count_ones` is 2 and '11' is in `arr`, otherwise `results` contains 'yes'. stdin is empty.
    for r in results:
        print(r)
        
    #State: `start` is an integer, `end` is an integer, `t` is 0, `n` is an integer, `arr` is a string, `_` is `t`, `count_ones` is an integer, `results` is a list containing either 'yes' or 'no' that must have at least `n` elements, `r` is the last element in the list, stdin is empty, and the last element in the list `results` which is either 'yes' or 'no' is being printed, and 'yes' or 'no' is printed `n` times.

#Overall this is what the function does:This function reads a series of binary strings from standard input, determines whether each string can be transformed into a string of alternating 1s and 0s by swapping two characters, and prints 'yes' if possible and 'no' otherwise. The function processes multiple test cases, where the number of test cases is provided as input, and each test case consists of a binary string. The function's output is a series of 'yes' or 'no' responses, one for each test case, indicating whether the corresponding binary string can be transformed into a string of alternating 1s and 0s.

