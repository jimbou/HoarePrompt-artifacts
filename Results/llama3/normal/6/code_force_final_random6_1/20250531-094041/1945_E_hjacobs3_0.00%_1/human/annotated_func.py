#State of the program right berfore the function call: array is a list of distinct integers from 1 to n in arbitrary order, find is an integer such that 1 <= find <= n and n is the length of array.
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: l is equal to r, and either array[l] is equal to find or array[l] is less than find and array[r] is greater than find.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings. The first string is the value of l + 1, where l is equal to r and either array[l] is equal to find or array[l] is less than find and array[r] is greater than find. The second string is the index of find in the array plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: l is equal to r, and either array[l] is equal to find or array[l] is less than find and array[r] is greater than find. l is equal to array.index(find), and this is printed: 0

#Overall this is what the function does:Searches for a target value in a sorted list of integers and returns the index of the target value and the index of the first element that is greater than or equal to the target value, or prints 0 if the target value is found at the expected index.

