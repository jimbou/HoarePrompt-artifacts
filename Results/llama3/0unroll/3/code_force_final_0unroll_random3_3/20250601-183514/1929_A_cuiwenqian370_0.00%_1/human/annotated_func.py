#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100 and arr is a list of n integers such that 1 <= arr[i] <= 10^9 for all i.
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
        
    #State: new_arr is a list of n integers such that new_arr[i] = arr[n-i-1] if i is even and new_arr[i] = arr[i//2] if i is odd, left is n, right is -1
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: Output State: `max_beauty` is the sum of the absolute differences between adjacent elements in the `new_arr` list, `left` is n, `right` is -1.
    return max_beauty
    #The program returns max_beauty which is the sum of the absolute differences between adjacent elements in the new_arr list.

#Overall this is what the function does:This function takes a list of integers as input, sorts it in ascending order, rearranges the elements in a specific alternating pattern, and then calculates the sum of the absolute differences between adjacent elements in the rearranged list. The function returns this sum, which represents the maximum beauty of the rearranged list.

