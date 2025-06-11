#State of the program right berfore the function call: sChar is a string consisting of only 0-s and/or 1-s, and its length is at least 2 and at most 2 * 10^5.
    s = []
    for i in sChar:
        s.append(i)
        
    #State: `sChar` is an empty string, `s` is a list containing all characters of the original `sChar` string, `i` is the last character in the original `sChar` string.
    left = 0
    cost = 0
    right = 1
    while left <= right and right < len(s) and (left < len(s)):
        if s[right] == '0' and s[left] == '1':
            s[right], s[left] = s[left], s[right]
            cost += right - left + 1
        
        while right < len(s) and s[right] != '0':
            right += 1
        
        while left < len(s) and s[left] != '1':
            left += 1
        
    #State: `sChar` is an empty string, `s` is a list containing all characters of the original `sChar` string, `i` is the last character in the original `sChar` string, `left` is equal to `len(s)`, `cost` is the total number of swaps performed, and `right` is equal to `len(s)`.
    return cost
    #The program returns the total number of swaps performed, which is initially 0 since `cost` is the total number of swaps performed.

#Overall this is what the function does:This function takes a string of 0s and 1s as input, swaps adjacent elements to move all 0s to the right and all 1s to the left, and returns the total number of swaps performed. The function modifies the input string in-place and returns the total number of swaps performed.

