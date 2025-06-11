#State of the program right berfore the function call: number is an integer
    return number % 1000000007
    #The program returns the remainder of the integer 'number' divided by 1000000007.

#Overall this is what the function does:This function takes an integer as input and returns the remainder of the integer divided by 1000000007. The input integer remains unchanged. The function's purpose is to perform a modulo operation on the input integer, and the final state of the program is the return of the calculated remainder.

#State of the program right berfore the function call: arr is a list of integers
    new_segment = []
    max_segment = [0, 0]
    segments_variants = []
    max_sum = -1
    for i in range(len(arr)):
        if new_segment:
            if arr[i] < 0:
                if max_segment[0] > new_segment[0]:
                    segments_variants.append(max_segment + [i - 1])
                else:
                    segments_variants.append(new_segment + [i - 1])
                    max_segment = new_segment
                new_segment = []
                max_segment[0] += arr[i]
            else:
                max_segment[0] += arr[i]
                new_segment[0] += arr[i]
        else:
            if arr[i] >= 0:
                new_segment = [arr[i], i]
            max_segment[0] += arr[i]
        
    #State: Output State: new_segment is an empty list, max_segment is a list containing the sum of all elements in arr and 0, segments_variants is a list of lists where each sublist contains the maximum sum of a segment of consecutive non-negative numbers in arr and the ending index of that segment, max_sum is -1, arr is unchanged.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: new_segment is an empty list, max_segment is a list containing the sum of all elements in arr and 0, segments_variants is a list of lists where each sublist contains the maximum sum of a segment of consecutive non-negative numbers in arr and the ending index of that segment, and two additional sublists: one containing the maximum sum of all elements in arr, 0, and the last index of arr, and another containing 0, the last index of arr, max_sum is -1, arr is unchanged, and total_max_segment is a list containing the maximum sum of all elements in arr and the last index of arr.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: *`new_segment` is an empty list, `max_segment` is a list containing the sum of all elements in `arr` and 0, `segments_variants` is a list of lists where each sublist contains the maximum sum of a segment of consecutive non-negative numbers in `arr` and the ending index of that segment, and two additional sublists: one containing the maximum sum of all elements in `arr`, 0, and the last index of `arr`, and another containing 0, the last index of `arr`, `max_sum` is -1, `arr` is unchanged, and `total_max_segment` is a list containing either the maximum sum of all elements in `arr` and the last index of `arr` or only one element, which is -1.
    return total_max_segment
    #The program returns a list containing either the maximum sum of all elements in `arr` and the last index of `arr`, or only one element, which is -1.

#Overall this is what the function does:This function takes a list of integers as input and returns a list containing either the maximum sum of all elements in the list and the last index of the list, or only one element, which is -1. The function identifies segments of consecutive non-negative numbers in the list, calculates their maximum sum, and keeps track of the maximum sum found so far. If no such segments are found, the function returns a list containing only -1. The input list remains unchanged throughout the function's execution.

#State of the program right berfore the function call: number is an integer and quantity is a non-negative integer
    answer = 0

#Overall this is what the function does:This function initializes a variable named "answer" to 0.

