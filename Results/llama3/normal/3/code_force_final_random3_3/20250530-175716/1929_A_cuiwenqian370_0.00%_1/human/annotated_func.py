#State of the program right berfore the function call: n is an integer greater than 1, arr is a list of n integers, all integers in arr are greater than 0.
    arr.sort()
    new_arr = []
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            new_arr.append(arr[left])
        else:
            new_arr.append(arr[right])
            new_arr.append(arr[left])
        
        left += 1
        
        right -= 1
        
    #State: n is an integer greater than 1, arr is a sorted list of n integers, all integers in arr are greater than 0, new_arr contains all elements of arr in reverse order, left is equal to n, right is equal to -1.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `n` is an integer greater than 1, `arr` is a sorted list of `n` integers, all integers in `arr` are greater than 0, `new_arr` contains all elements of `arr` in reverse order, `left` is equal to `n`, `right` is equal to -1, `max_beauty` is equal to the sum of the absolute differences between consecutive elements in `new_arr`, `i` is equal to `n-1`.
    return max_beauty
    #The program returns max_beauty which is equal to the sum of the absolute differences between consecutive elements in new_arr, where new_arr contains all elements of arr in reverse order, arr is a sorted list of n integers, all integers in arr are greater than 0, and n is an integer greater than 1.

#Overall this is what the function does:This function calculates the maximum beauty of a given list of integers. It first sorts the list in ascending order, then reverses the order of the elements. It then calculates the sum of the absolute differences between consecutive elements in the reversed list. The function returns this sum, which represents the maximum beauty of the input list.

