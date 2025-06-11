#State of the program right berfore the function call: n is an integer greater than or equal to 2 and less than or equal to 100, and arr is a list of n integers, each integer is greater than or equal to 1 and less than or equal to 10^9.
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
        
    #State: left is n, right is -1, and new_arr is a list of n integers where the first half of the list contains the elements of arr in reverse order, and the second half of the list contains the elements of arr in the original order, but with the middle element (if n is odd) appended only once.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: left is n, right is -1, new_arr is a list of n integers where the first half of the list contains the elements of arr in reverse order, and the second half of the list contains the elements of arr in the original order, but with the middle element (if n is odd) appended only once, and max_beauty is the sum of the absolute differences between consecutive elements in new_arr.
    return max_beauty
    #The program returns the sum of the absolute differences between consecutive elements in the list `new_arr`, which contains the elements of `arr` in reverse order in the first half and in the original order in the second half, with the middle element appended only once if `n` is odd.

#Overall this is what the function does:This function takes an integer n and a list of n integers as input, rearranges the list in a specific order (reverse order in the first half and original order in the second half, with the middle element appended only once if n is odd), and returns the sum of the absolute differences between consecutive elements in the rearranged list.

