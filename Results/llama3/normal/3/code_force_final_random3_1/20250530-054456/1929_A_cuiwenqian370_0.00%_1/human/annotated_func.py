#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, and arr is a list of n integers such that 1 <= arr[i] <= 10^9 for all i.
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
        
    #State: new_arr is a list containing all the elements of arr in reverse order, left is n, and right is -1.
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
        
    #State: `max_beauty` is increased by the sum of the absolute differences between consecutive elements of `arr` in reverse order, `new_arr` is a list containing all the elements of `arr` in reverse order, `left` is `n`, `right` is -1, `n` is greater than or equal to 1, `i` is `n-1`.
    return max_beauty
    #The program returns max_beauty, which is increased by the sum of the absolute differences between consecutive elements of arr in reverse order.

#Overall this is what the function does:This function takes a list of integers and an integer n as input, sorts the list in ascending order, rearranges the sorted list in a specific order (alternating between the largest and smallest remaining elements), and then calculates the sum of the absolute differences between consecutive elements in the rearranged list. The function returns this sum, which represents the maximum beauty of the rearranged list.

