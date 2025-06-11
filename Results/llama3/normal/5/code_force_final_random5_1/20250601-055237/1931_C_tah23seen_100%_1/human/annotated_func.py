#State of the program right berfore the function call: arr is a list of integers.
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: arr is a list of integers where the first i+1 elements are the same, i is the number of consecutive equal elements at the start of arr, n is the length of arr, j is the last index of arr.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: arr is a list of integers where the first i+1 elements are the same, i is the number of consecutive equal elements at the start of arr, n is greater than 1, and all elements of arr are equal, j is -1.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns 0
    #State: arr is a list of integers where the first i+1 elements are the same, i is the number of consecutive equal elements at the start of arr, n is greater than 1, all elements of arr are equal, j is -1, and the first element of arr is not equal to the last element of arr.
    return max(min(n - i - 1, j), 0)
    #The program returns 0

#Overall this is what the function does:This function calculates the maximum number of consecutive equal elements that can be removed from the start and end of a list of integers, without removing all elements. It returns 0 if the list has only one element or all elements are equal, otherwise it returns the maximum number of elements that can be removed.

