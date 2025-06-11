#State of the program right berfore the function call: sChar is a string consisting of only 0-s and/or 1-s, and its length is between 2 and 2 * 10^5 (inclusive).
    s = []
    for i in sChar:
        s.append(i)
        
    #State: `sChar` is a string consisting of only 0-s and/or 1-s, and its length is between 2 and 2 * 10^5 (inclusive), `s` is a list containing all characters of `sChar`, `i` is the last character in the string
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
        
    #State: left is equal to len(s), right is equal to len(s), s[right-1] is not equal to '0', s[left-1] is not equal to '1'
    return cost
    #The program returns cost

#Overall this is what the function does:This function takes a string of 0s and 1s as input, swaps adjacent 0s and 1s in the string from left to right, and returns the total number of swaps performed. The function modifies the input string in-place by swapping the characters. The final state of the program is that the input string has been modified to have all 0s on the right and all 1s on the left, and the total number of swaps performed is returned as the cost.

