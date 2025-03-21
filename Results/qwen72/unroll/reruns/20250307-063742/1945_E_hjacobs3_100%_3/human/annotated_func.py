#State of the program right berfore the function call: array is a list of integers representing a permutation of size n (1 ≤ n ≤ 2·10^5) where all elements are distinct and in the range [1, n], and find is an integer (1 ≤ find ≤ n) that needs to be found in the permutation.
def func_1(array, find):
    n = len(array)
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        
        if array[mid] <= find:
            l = mid
        else:
            r = mid
        
    #State: `l` is the largest index such that `array[l] <= find`, and `r` is the smallest index such that `array[r] > find`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two string elements: the first element is the string representation of `l + 1`, where `l` is the largest index such that `array[l] <= find`; the second element is the string representation of the index of `find` in the `array` plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: *`l` is the largest index such that `array[l] <= find`, and `r` is the smallest index such that `array[r] > find`. `l` is equal to the index of `find` in `array`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `array` and an integer `find`. It returns a list of two strings: the first string is the string representation of `l + 1`, where `l` is the largest index such that `array[l] <= find`; the second string is the string representation of the index of `find` in `array` plus 1. If `l` is not equal to the index of `find` in `array`, it prints `1`; otherwise, it prints `0`. The function modifies the values of `l` and `r` during its execution, but these changes are not reflected outside the function.

